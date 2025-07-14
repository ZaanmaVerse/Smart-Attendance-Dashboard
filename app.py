from flask import Flask, render_template, request
import pandas as pd
from src.data_processing import summarize_attendance, prepare_chart_data
from src.bolos_detection import detect_potential_truants, detect_bolos_on_specific_days
from flask import send_file, make_response
import io
from xhtml2pdf import pisa


app = Flask(__name__)

@app.route('/download/excel')
def download_excel():
    df = pd.read_csv('data/attendance_data.csv')
    summary = summarize_attendance(df)

    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        summary.to_excel(writer, index=False, sheet_name='Rekap Absensi')
    output.seek(0)

    return send_file(output,
                    download_name="rekap_absensi.xlsx",
                    as_attachment=True,
                    mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

@app.route('/download/pdf')
def download_pdf():
    df = pd.read_csv('data/attendance_data.csv')
    summary = summarize_attendance(df)

    html = render_template("export_pdf_template.html", data=summary.to_dict(orient='records'))
    result = io.BytesIO()
    pisa.CreatePDF(io.StringIO(html), dest=result)
    result.seek(0)

    return send_file(result, download_name="rekap_absensi.pdf", as_attachment=True)
@app.route('/')
def index():
    # Load data absensi
    df = pd.read_csv('data/attendance_data.csv')
    df['Tanggal'] = pd.to_datetime(df['Tanggal'])

    # Ambil filter karyawan dari query string
    selected_id = request.args.get('id', None)

    # Filter berdasarkan ID (jika dipilih)
    if selected_id and selected_id != "ALL":
        df = df[df['ID'].astype(str) == selected_id]

    # Hitung metrik kehadiran
    total_karyawan = df['ID'].nunique()
    total_hadir = (df['Status'] == 'Hadir').sum()
    total_alfa = (df['Status'] == 'Alfa').sum()
    total_sakit = (df['Status'] == 'Sakit').sum()

    # Untuk Pie Chart
    status_counts = {
        "Hadir": total_hadir,
        "Alfa": total_alfa,
        "Sakit": total_sakit
    }

    # Proses data lainnya
    summary = summarize_attendance(df)
    suspects = detect_potential_truants(df)
    pola = detect_bolos_on_specific_days(df)
    chart_data = prepare_chart_data(df)

    # Data untuk dropdown filter karyawan
    df_all = pd.read_csv('data/attendance_data.csv')
    df_all['Nama'] = df_all['Nama'].astype(str)
    karyawan_list = df_all[['ID', 'Nama']].drop_duplicates().sort_values('Nama')

    # Render HTML
    return render_template('index.html',
        total_karyawan=total_karyawan,
        total_hadir=total_hadir,
        total_alfa=total_alfa,
        total_sakit=total_sakit,
        summary=summary.to_dict(orient='records'),
        suspects=suspects.to_dict(orient='records'),
        pola=pola.to_dict(orient='records'),
        chart_labels=chart_data['Hari'].tolist(),
        chart_values=chart_data['Jumlah Alfa'].tolist(),
        status_counts=status_counts,
        selected_id=selected_id,
        karyawan_list=karyawan_list.to_dict(orient='records')
    )

if __name__ == '__main__':
    app.run(debug=True)
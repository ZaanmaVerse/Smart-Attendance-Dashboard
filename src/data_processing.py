import pandas as pd

def load_attendance_data(path='../data/attendance_data.csv'):
    try:
        df = pd.read_csv(path)
        df['Tanggal'] = pd.to_datetime(df['Tanggal'], errors='coerce')
        df = df.dropna(subset=['Tanggal'])  # Hapus baris yang tanggalnya invalid
        df = df.sort_values(by=['ID', 'Tanggal'])
        return df
    except Exception as e:
        print(f"[ERROR] Gagal memuat data: {e}")
        return pd.DataFrame()

def summarize_attendance(df):
    if df.empty:
        return pd.DataFrame()
    
    summary = (
        df.groupby(['ID', 'Nama'])['Status']
        .value_counts()
        .unstack(fill_value=0)
        .reset_index()
    )

    # Pastikan semua kolom ada
    for status in ['Hadir', 'Alfa', 'Sakit']:
        if status not in summary.columns:
            summary[status] = 0

    return summary

def prepare_chart_data(df):
    if df.empty:
        return pd.DataFrame(columns=['Hari', 'Jumlah Alfa'])
    
    df['Hari'] = df['Tanggal'].dt.strftime('%a')  # Sen, Sel, Rab, ...
    chart_data = (
        df[df['Status'] == 'Alfa']
        .groupby('Hari')
        .size()
        .reset_index(name='Jumlah Alfa')
        .sort_values(by='Hari')
    )

    return chart_data
import pandas as pd

# Deteksi karyawan dengan jumlah Alfa di atas ambang batas (misalnya 3)
def detect_potential_truants(df, threshold=3):
    if df.empty:
        return pd.DataFrame()
    
    alpha_count = df[df['Status'] == 'Alfa'].groupby(['ID', 'Nama']).size().reset_index(name='Alfa')
    suspicious = alpha_count[alpha_count['Alfa'] >= threshold]
    return suspicious

# Deteksi karyawan yang sering bolos di hari Senin atau Jumat
def detect_bolos_on_specific_days(df, hari_list=['Monday', 'Friday']):
    if df.empty:
        return pd.DataFrame()

    df['DayName'] = df['Tanggal'].dt.day_name()
    alpha_days = df[(df['Status'] == 'Alfa') & (df['DayName'].isin(hari_list))]
    
    result = (
        alpha_days
        .groupby(['ID', 'Nama', 'DayName'])
        .size()
        .reset_index(name='Alfa')
        .sort_values(by='Alfa', ascending=False)
    )

    return result
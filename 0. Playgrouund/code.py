import pandas as pd

def date_and_time(file_path: str) -> None:
    # playing with date and time (panda only can handle 1677 to 2262 year)
    df = pd.read_excel(file_path)
    df['date_time'] = pd.to_datetime(df['date_time'], format='%m-%d-%Y %H:%M:%S', errors='coerce')
    df['year'] = df['date_time'].dt.year
    df['month'] = df['date_time'].dt.month
    df['date'] = df['date_time'].dt.date
    df['hour:minute'] = df['date_time'].dt.strftime('%H:%M')
    df['month-date'] = df['date_time'].dt.strftime('%m-%d')
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name='result', index=False)


if __name__ == "__main__":
    # date_and_time(r'C:\AI\0. Playgrouund\sampledata.xlsx')
import pandas as pd

def handle_missing_data(file_path: str) -> None:
    df = pd.read_excel(file_path)
    df = df.dropna(how='all', subset=df.columns[1:])
    df = df.dropna(axis=1, how='all')
    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        mean_value = df[col].mean()
        df[col] = df[col].fillna(mean_value)

    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name='result', index=False)


if __name__ == "__main__":
    handle_missing_data(r'C:\AI\2. Handling Missing Data\4. Dropping rows, columns, imputation\sampledata.xlsx')
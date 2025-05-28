import pandas as pd

def handle_missing_data(file_path: str) -> None:
    # Step 1: Read the Excel file
    df = pd.read_excel(file_path)

    # Step 2: Drop rows where all but 'Name' are missing
    df = df.dropna(how='all', subset=df.columns[1:])

    # Step 3: Drop columns where all values are missing
    df = df.dropna(axis=1, how='all')

    # Step 4: Fill missing values with mean (numeric columns only)
    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        mean_value = df[col].mean()
        df[col] = df[col].fillna(mean_value)

    # Step 5: Remove existing 'result' sheet if exists, and write new one
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name='result', index=False)


if __name__ == "__main__":
    handle_missing_data(r'C:\AI\1. Data Exploration and Preprocessing\4. Dropping rows, columns, imputation\sampledata.xlsx')
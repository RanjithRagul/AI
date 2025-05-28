import pandas as pd

def clean_sales_data(file_path: str) -> None:
    # Step 1: Read Excel file
    df = pd.read_excel(file_path, sheet_name=0)

    # Step 2: Drop rows where 'Quantity' is missing
    df = df.dropna(subset=['Quantity'])

    # Step 3: Filter where 'Price' > 100
    df = df[df['Price'] > 100]

    # Step 4: Create new column 'Total'
    df['Total'] = df['Price'] * df['Quantity']

    # Step 5: Remove existing 'result' sheet if exists, and write new one
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name='result', index=False)


if __name__ == "__main__":
    clean_sales_data(r'C:\AI\1. Data Exploration and Preprocessing\3. Basic filtering and manipulation\sampledata.xlsx')
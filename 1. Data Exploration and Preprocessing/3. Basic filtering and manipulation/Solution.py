import pandas as pd

def clean_sales_data(file_path: str) -> None:
    df = pd.read_excel(file_path, sheet_name=0)
    df = df.dropna(subset=['Quantity'])
    df = df[df['Price'] > 100]
    df['Total'] = df['Price'] * df['Quantity']
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name='result', index=False)

if __name__ == "__main__":
    clean_sales_data(r'C:\AI\1. Data Exploration and Preprocessing\3. Basic filtering and manipulation\sampledata.xlsx')
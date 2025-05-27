import pandas as pd
from openpyxl import load_workbook

def analyze_customer_data(file_path: str) -> None:
    # Step 1: Load data from the 'customers' sheet
    df = pd.read_excel(file_path, sheet_name="data")

    # Step 2: Perform basic analysis
    total_customers = len(df)  # Count the number of customers
    average_age = df["Age"].mean()  # Calculate average age
    total_purchase = df["PurchaseAmount"].sum()  # Calculate total purchase amount
    top_spender = df.loc[df["PurchaseAmount"].idxmax(), "Name"]  # Find the top spender's name

    # Step 3: Prepare result rows for Excel
    results = [
        ["Metric", "Value"],
        ["Total Customers", total_customers],
        ["Average Age", average_age],
        ["Total Purchase Amount", total_purchase],
        ["Top Spender", top_spender]
    ]

    # Step 4: Load workbook and update 'result' sheet
    book = load_workbook(file_path)
    if "result" in book.sheetnames:
        book.remove(book["result"]) 
    result_ws = book.create_sheet("result") 

    # Step 5: Write the results to the new sheet
    for row in results:
        result_ws.append(row)

    # Step 6: Save the workbook
    book.save(file_path)



if __name__ == "__main__":
    analyze_customer_data(r'C:\AI\Part1\1. Understanding dataset structure, sample records\sampledata.xlsx')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore
import openpyxl

def detect_outliers(file_path):
    df = pd.read_excel(file_path, sheet_name=0)
    df['Z_score'] = zscore(df['Sales'])
    df['Z_outlier'] = df['Z_score'].abs() > 3
    Q1 = df['Sales'].quantile(0.25)
    Q3 = df['Sales'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df['IQR_outlier'] = (df['Sales'] < lower_bound) | (df['Sales'] > upper_bound)
    plt.figure(figsize=(6, 4))
    plt.boxplot(df['Sales'])
    plt.title("Boxplot of Apple Sales")
    plt.ylabel("Sales")
    plt.grid(True)
    plt.savefig("boxplot_sales.png")  # Save image if needed
    plt.close()
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name='result', index=False)

if __name__ == "__main__":
    detect_outliers(r'C:\AI\3. Outlier Detection\sampledata.xlsx')
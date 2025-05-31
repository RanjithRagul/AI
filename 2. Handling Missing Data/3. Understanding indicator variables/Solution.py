import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

def impute_weather_data(file_path: str) -> None:
    df = pd.read_excel(file_path)
    indicator_column = 'Smoker_Indicator'
    df[indicator_column] = df['Smoker'].map(lambda x: 1 if x == 'Yes' else 0 if x == 'No' else np.nan)
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name='result', index=False)


if __name__ == "__main__":
    impute_weather_data(r'C:\AI\2. Handling Missing Data\3. Understanding indicator variables\sampledata.xlsx')
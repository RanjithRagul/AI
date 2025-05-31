import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

def impute_weather_data(file_path: str) -> None:
    k = 5 # kTh near
    df = pd.read_excel(file_path)
    if np.issubdtype(df['Time'].dtype, np.number):
        df['Time'] = pd.to_datetime(df['Time'], origin='1899-12-30', unit='d').dt.time
    else:
        df['Time'] = pd.to_datetime(df['Time'], format='%H:%M', errors='coerce').dt.time
    df = df.sort_values(by='Time').reset_index(drop=True)
    df['Temperature'] = df['Temperature'].interpolate(method='linear')
    knn_imputer = KNNImputer(n_neighbors=k)
    df[['Temperature', 'Humidity']] = knn_imputer.fit_transform(df[['Temperature', 'Humidity']])
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name='result', index=False)


if __name__ == "__main__":
    impute_weather_data(r'C:\AI\2. Handling Missing Data\2. Advanced methods-KNN Imputation, Interpolation\sampledata.xlsx')
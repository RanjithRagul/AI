import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
import openpyxl

def scale_features(file_path: str) -> None:
    df = pd.read_excel(file_path, sheet_name=0)
    std_scaler = StandardScaler()
    minmax_scaler = MinMaxScaler()
    robust_scaler = RobustScaler()
    df['height_scaled'] = std_scaler.fit_transform(df[['height']])
    df['weight_scaled'] = minmax_scaler.fit_transform(df[['weight']])
    df['income_scaled'] = robust_scaler.fit_transform(df[['income']])
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name='result', index=False)


if __name__ == "__main__":
    scale_features(r'C:\AI\4. Feature Scaling\sampledata.xlsx')
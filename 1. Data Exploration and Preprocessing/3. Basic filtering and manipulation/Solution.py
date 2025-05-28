import pandas as pd

def analyze_data_types_and_distribution(filename):
    # Read the Excel file
    df = pd.read_excel(filename, sheet_name=0)

    result = []

    for col in df.columns:
        col_data = df[col]
        data_type = None
        distribution = "N/A"

        # Identify data type
        if pd.api.types.is_numeric_dtype(col_data):
            data_type = 'numeric'
        elif pd.api.types.is_datetime64_any_dtype(col_data):
            data_type = 'datetime'
        elif pd.api.types.is_bool_dtype(col_data):
            data_type = 'boolean'
        else:
            data_type = 'categorical'

        # If numeric, check distribution
        if data_type == 'numeric':
            col_clean = col_data.dropna()
            if len(col_clean) > 0:
                mean = col_clean.mean()
                median = col_clean.median()
                std = col_clean.std()
                min_val = col_clean.min()
                max_val = col_clean.max()

                # Simple heuristics for distribution
                if abs(mean - median) < 0.1 * std:
                    distribution = 'normal'
                elif std < 0.1 * (max_val - min_val):
                    distribution = 'uniform'
                else:
                    distribution = 'skewed'

        result.append([col, data_type, distribution])

    result_df = pd.DataFrame(result, columns=["Column Name", "Data Type", "Distribution"])

    # Remove existing 'result' sheet if present and write new one
    with pd.ExcelWriter(filename, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        result_df.to_excel(writer, sheet_name='result', index=False)


if __name__ == "__main__":
    analyze_data_types_and_distribution(r'C:\AI\1. Data Exploration and Preprocessing\2. Identifying data types, distributions\sampledata.xlsx')
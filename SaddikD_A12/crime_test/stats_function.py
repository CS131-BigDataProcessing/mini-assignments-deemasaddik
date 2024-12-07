def calculate_mean(column):

    if 'Vict Age' not in df.columns:
        raise ValueError("Missing 'Vict Age' column")

    numeric_data = pd.to_numeric(df['Vict Age'], errors='coerce')
    valid_data = numeric_data.dropna()

    if valid_data.empty:
        raise ValueError("No valid numeric data in 'Vict Age'")
        
    return valid_data.mean()


def calculate_median(column):
    
    if 'Vict Age' not in df.columns:
        raise ValueError("Missing 'Vict Age' column")

    numeric_data = pd.to_numeric(df['Vict Age'], errors='coerce')
    valid_data = numeric_data.dropna()

    if valid_data.empty:
        raise ValueError("No valid numeric data in 'Vict Age'")
        
    return valid_data.median()

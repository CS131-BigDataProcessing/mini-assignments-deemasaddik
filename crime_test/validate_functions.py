import pandas as pd

def validate_vict_sex(column):
    # Validate 'Vict sex' column. Check that values are either 'M' or 'F' and not missing (NULL).
    if column.isnull().any():
        return False
    return all(column.isin(['M', 'F']))

def validate_vict_age(column):
   # Validate 'Vict age' column. Check that values are between 1 and 100 and not missing (NULL).
    if column.isnull().any():
        return False
    return all((column >= 1) & (column <= 100))

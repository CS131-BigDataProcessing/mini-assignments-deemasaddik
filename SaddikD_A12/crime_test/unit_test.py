import pandas as pd 
import pytest
from validate_functions import validate_vict_sex, validate_vict_age
from stats_function import calculate_mean, calculate_median
data = pd.read_csv("./Crime_Data_from_2020_to_Present.csv")
def test_validate_vict_sex(sex_column):
    if sex_column.isnull().any():
        print("Validation failed: 'Vict sex' contains null values.")
        return False
    if not all(sex_column.isin(['M', 'F'])):
        print("Validation failed: 'Vict sex' contains invalid values.")
        return False
    return True

def test_validate_vict_age(age_column):
    if age_column.isnull().any():
        print("Validation failed: 'Vict age' contains null values.")
        return False
    if not all(age_column.between(1, 100)):
        print("Validation failed: 'Vict age' contains values out of range (1-100).")
        return False
    return True

def test_calculate_mean(age_column):
    if age_column.empty:
        raise ValueError("The 'Vict age' column is empty.")
    return age_column.mean()

def test_calculate_median(age_column):
    if age_column.empty:
        raise ValueError("The 'Vict age' column is empty.")
    return age_column.median()

def test_calculate_mean_edge_case():
    df = pd.DataFrame({'Vict age': ['eight', None]})
    with pytest.raises(TypeError):
        calculate_mean(df['Vict age'])

if validate_vict_sex(data['Vict sex']):
    print("'Vict sex' column is valid.")

if validate_vict_age(data['Vict age']):
    print("'Vict age' column is valid.")

try:
    mean_age = calculate_mean(data['Vict age'])
    median_age = calculate_median(data['Vict age'])
    print(f"Mean age: {mean_age}")
    print(f"Median age: {median_age}")
except Exception as e:
    print(f"Error calculating statistics: {e}")

# Edge case test for mean calculation
def test_calculate_mean_edge_case():
    df = pd.DataFrame({'Vict age': ['eight', None]})
    with pytest.raises(TypeError):
        calculate_mean(df['Vict age'])

# Run edge case test
if __name__ == "__main__":
    test_calculate_mean_edge_case()


import pandas as pd
import pytest
from validate_functions import validate_vict_sex, validate_vict_age
from stats_function import calculate_mean, calculate_median
import zipfile

# Path to the ZIP file
zip_file_path = "./Crime_Data_from_2020_to_Present.zip"

# Open the ZIP file and read the CSV
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # List files in the ZIP archive
    file_list = zip_ref.namelist()
    print("Files in ZIP:", file_list)
    
    # Assuming the ZIP contains a single CSV, read it
    csv_file_name = file_list[0]  # Adjust if multiple files are present
    with zip_ref.open(csv_file_name) as csv_file:
        data = pd.read_csv(csv_file)

# Validate 'Vict sex' column
def test_validate_vict_sex(sex_column):
    assert sex_column.isnull().sum() == 0, "Validation failed: 'Vict sex' contains null values."
    assert sex_column.isin(['M', 'F']).all(), "Validation failed: 'Vict sex' contains invalid values."

# Validate 'Vict age' column
def test_validate_vict_age(age_column):
    assert age_column.isnull().sum() == 0, "Validation failed: 'Vict age' contains null values."
    assert age_column.between(1, 100).all(), "Validation failed: 'Vict age' contains values out of range (1-100)."

# Mean and Median Calculations
def test_calculate_mean(age_column):
    if age_column.empty:
        raise ValueError("The 'Vict age' column is empty.")
    return age_column.mean()

def test_calculate_median(age_column):
    if age_column.empty:
        raise ValueError("The 'Vict age' column is empty.")
    return age_column.median()

# Edge case test for mean calculation
def test_calculate_mean_edge_case():
    df = pd.DataFrame({'Vict age': ['eight', None]})
    with pytest.raises(TypeError):
        calculate_mean(df['Vict age'])

# Main validation and calculation code
if __name__ == "__main__":
    # Run validations
    try:
        test_validate_vict_sex(data['Vict sex'])
        print("'Vict sex' column is valid.")
    except AssertionError as e:
        print(e)

    try:
        test_validate_vict_age(data['Vict age'])
        print("'Vict age' column is valid.")
    except AssertionError as e:
        print(e)

    # Calculate statistics
    try:
        mean_age = test_calculate_mean(data['Vict age'])
        median_age = test_calculate_median(data['Vict age'])
        print(f"Mean age: {mean_age}")
        print(f"Median age: {median_age}")
    except Exception as e:
        print(f"Error calculating statistics: {e}")

    # Run edge case test
    test_calculate_mean_edge_case()

import pandas as pd
import zipfile
import pytest
from validate_functions import validate_vict_sex, validate_vict_age
from stats_function import calculate_mean, calculate_median

# Path to the ZIP file
zip_file_path = "./Crime_Data_from_2020_to_Present.zip"

# Open the ZIP file and read the CSV
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # List files in the ZIP archive
    file_list = zip_ref.namelist()
    print("Files in ZIP:", file_list)
    
    # Assuming the ZIP contains a single CSV, read it
    # We will open the first CSV file found in the ZIP (you can change the index if needed)
    csv_file_name = file_list[0]  # If there are multiple CSVs, adjust this as needed
    with zip_ref.open(csv_file_name) as csv_file:
        data = pd.read_csv(csv_file)

# Validate 'Vict sex' column
def test_validate_vict_sex():
    sex_column = data['Vict sex']
    assert sex_column.isnull().sum() == 0, "Validation failed: 'Vict sex' contains null values."
    assert sex_column.isin(['M', 'F']).all(), "Validation failed: 'Vict sex' contains invalid values."

# Validate 'Vict age' column
def test_validate_vict_age():
    age_column = data['Vict age']
    assert age_column.isnull().sum() == 0, "Validation failed: 'Vict age' contains null values."
    assert age_column.between(1, 100).all(), "Validation failed: 'Vict age' contains values out of range (1-100)."

# Mean and Median Calculations
def test_calculate_mean():
    age_column = data['Vict age']
    if age_column.empty:
        raise ValueError("The 'Vict age' column is empty.")
    mean_age = calculate_mean(age_column)  # Assuming calculate_mean returns the mean
    expected_mean = age_column.mean()  # You can calculate it manually to compare
    assert mean_age == expected_mean, f"Expected mean {expected_mean} but got {mean_age}"

def test_calculate_median():
    age_column = data['Vict age']
    if age_column.empty:
        raise ValueError("The 'Vict age' column is empty.")
    median_age = calculate_median(age_column)  # Assuming calculate_median returns the median
    expected_median = age_column.median()  # You can calculate it manually to compare
    assert median_age == expected_median, f"Expected median {expected_median} but got {median_age}"

# Edge case test for mean calculation with invalid data
def test_calculate_mean_edge_case():
    df = pd.DataFrame({'Vict age': ['eight', None]})
    with pytest.raises(TypeError):
        calculate_mean(df['Vict age'])

# Main validation and calculation code
if __name__ == "__main__":
    # Run validations
    try:
        test_validate_vict_sex()  # Now it uses the local data
        print("'Vict sex' column is valid.")
    except AssertionError as e:
        print(e)

    try:
        test_validate_vict_age()  # Now it uses the local data
        print("'Vict age' column is valid.")
    except AssertionError as e:
        print(e)

    # Calculate statistics
    try:
        test_calculate_mean()  # Now it runs the test
        test_calculate_median()  # Now it runs the test
        print("Mean and Median calculations are correct.")
    except Exception as e:
        print(f"Error calculating statistics: {e}")

    # Run edge case test
    test_calculate_mean_edge_case()  # This will check for edge cases

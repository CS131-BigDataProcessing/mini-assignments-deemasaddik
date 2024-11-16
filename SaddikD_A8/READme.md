# Data Cleaning Script for Airbnb NYC 2019 Dataset

## Overview

This Bash script performs data cleaning operations on the Airbnb NYC 2019 dataset. It handles various data quality issues such as missing values, duplicates, and outliers.

## Prerequisites

- Bash shell
- AWK
- sed
- bc (basic calculator)

## Input

- `AB_NYC_2019.csv`: The original dataset file

## Output

- `cleaned_AB_NYC_2019.csv`: The final cleaned dataset
- `missing_values.csv`: Lines with missing values
- `remove_missing.csv`: Dataset with rows containing missing values removed
- `replace_na.csv`: Dataset with missing values replaced by "NA"
- `removed_duplicates.csv`: Dataset with duplicate entries removed
- `price_outliers.txt`: List of identified price outliers

## Usage

1. Ensure the input file `AB_NYC_2019.csv` is in the same directory as the script.
2. Make the script executable:
chmod +x script_name.sh
3. Run the script:
./script_name.sh


## Cleaning Steps

1. Remove trailing spaces and newlines from each line
2. Identify and save lines with missing values
3. Remove rows with missing values
4. Replace missing values with "NA" in a separate file
5. Remove duplicate entries
6. Identify and handle outliers in the Price column
7. Replace high outliers in the Price column with the median value

## Notes

- The script assumes the Price column is the 10th column in the CSV file.
- Outliers are identified using the Interquartile Range (IQR) method.
- Only high outliers (above Q3 + 1.5 * IQR) are replaced with the median.

## Customization

To adapt this script for other datasets:
- Modify the `INPUT_FILE` and `OUTPUT_FILE` variables as needed.
- Adjust the column number in steps involving the Price column (currently set to column 10).
- Modify the outlier handling logic if different treatment is required.


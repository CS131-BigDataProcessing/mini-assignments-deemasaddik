#!/bin/bash
# Define input and output files
INPUT_FILE="AB_NYC_2019.csv"
OUTPUT_FILE="cleaned_AB_NYC_2019.csv"

# Step 1: Remove trailing spaces and newlines from each line in the CSV
echo "Removing trailing spaces and newlines..."
sed -i 's/[[:space:]]*$//' "$INPUT_FILE"

# Step 2: Identify missing values and save lines with missing values to a CSV file
echo "Identifying rows with missing values and saving to missing_values.csv..."
awk -F',' 'NF < 16 { print "Line", NR ":", $0 }' "$INPUT_FILE" > missing_values.csv

# Step 3: Remove rows with missing values and save to a file
echo "Removing rows with missing values..."
awk -F, '{
    has_missing=0
    for(i=1; i<=NF; i++) {
        if($i == "") {
            has_missing=1
            break
        }
    }
    if(has_missing==0) {
        print $0
    }
}' "$INPUT_FILE" > remove_missing.csv

# Step 4: Replace missing values with "NA" in another file
echo "Replacing missing values with 'NA'..."
awk -F, '{
    for(i=1; i<=NF; i++) {
        if($i == "") {
            $i="NA"
        }
    }
    print $0
}' OFS=',' "$INPUT_FILE" > replace_na.csv

# Step 5: Remove duplicate entries from the file without missing values
echo "Removing duplicate entries..."
awk '!seen[$0]++' remove_missing.csv > removed_duplicates.csv

# Step 6: Identify and handle outliers in a specified column (e.g., Price)
echo "Calculating outliers based on IQR for Price column..."

# Extract the specified column (assumed to be column 10) and sort it
awk -F',' '{print $10}' removed_duplicates.csv | sort -n > sorted_data.txt

# Calculate the number of lines
total_lines=$(wc -l < sorted_data.txt)

# Calculate Q1 and Q3 using sed to retrieve values
q1_line=$(echo "$total_lines * 0.25" | bc | awk '{print int($1)}')
q1=$(sed "${q1_line}q;d" sorted_data.txt)

q3_line=$(echo "$total_lines * 0.75" | bc | awk '{print int($1)}')
q3=$(sed "${q3_line}q;d" sorted_data.txt)

# Calculate the IQR (Interquartile Range)
iqr=$(echo "$q3 - $q1" | bc)

# Identify and save outliers based on the calculated IQR
echo "Identifying outliers and saving to price_outliers.txt..."
awk -F, -v Q1="$q1" -v Q3="$q3" -v IQR="$iqr" '{
    if ($10 < (Q1 - 1.5 * IQR) || $10 > (Q3 + 1.5 * IQR)) {
        print $10
    }
}' removed_duplicates.csv > price_outliers.txt

# Step 7: Replace high outliers with the median in the Price column
echo "Replacing high outliers in the Price column with the median value..."

# Calculate the median
median=$(awk '{ a[NR] = $0 } END { if (NR % 2) { print a[(NR + 1) / 2] } else { print (a[(NR / 2)] + a[(NR / 2) + 1]) / 2 } }' sorted_data.txt)

# Replace high outliers with the median in the specified column
awk -F',' -v med="$median" -v Q1="$q1" -v Q3="$q3" -v IQR="$iqr" '{
    if ($10 > (Q3 + 1.5 * IQR)) {
        $10 = med
    }
    print $0
}' OFS=',' removed_duplicates.csv > "$OUTPUT_FILE"

echo "Data cleaning complete. Cleaned dataset saved as $OUTPUT_FILE."


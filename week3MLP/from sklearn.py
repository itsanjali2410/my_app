import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer

# Step 1: Load the dataset
df = pd.read_csv("DataPreprocessingGraded_dataset.csv")
Blank_values = (df == "?").sum()
print(Blank_values)
# Step 2: Identify numeric and non-numeric columns
numeric_column = df.select_dtypes(include=[np.number]).columns
non_numeric_columns = df.select_dtypes(exclude=[np.number]).columns

# Step 3: Replace "?" with NaN in all columns
df[numeric_column] = df[numeric_column].replace("?", np.nan)

# Step 4: Impute missing values in numeric columns using the mean
imputer = SimpleImputer(strategy="mean")
df[numeric_column] = imputer.fit_transform(df[numeric_column])

# Step 5: Impute missing values in non-numeric columns using the most frequent value
imputer_cat = SimpleImputer(strategy="most_frequent")
df[non_numeric_columns] = imputer_cat.fit_transform(df[non_numeric_columns])

# Step 6: Save the modified DataFrame to a CSV file
df.to_csv('modified_data.csv', index=False)

# Step 7: Calculate the variance of the numeric columns after imputation
for_variance = df[numeric_column].var()

# Print the variance of the numeric columns
print("Variance of numeric columns:")
print(for_variance)

# Replace "?" with NaN in the 'V2' column
df['V2'] = df['V2'].replace("?", np.nan)

# Initialize the SimpleImputer to replace missing values with the mean of the column
imputer = SimpleImputer(strategy="mean")

# Apply the imputer to the 'V2' column
df['V2'] = imputer.fit_transform(df[['V2']])

# Calculate the average (mean) of the 'V2' column after imputation
average_v2 = df['V2'].mean()

# Print the result
print(f"Average of 'V2' after imputation: {average_v2}")


df['V1'] = df['V1'].replace("?", np.nan)
imputer = SimpleImputer(strategy="median")

df["V1"] = imputer.fit_transform(df[["V1"]])
average_v1 = df["V1"].mean()
print(f"Median of 'V1' after imputation: {average_v1}")

# after applying KNNimputer
knn_imputer = KNNImputer(n_neighbors = 3)

df["V1"] = knn_imputer.fit_transform(df[["V1"]])

v1_average = df['V1'].mean()
print(f"Average of 'V1' after applying KNNImputer: {v1_average}")


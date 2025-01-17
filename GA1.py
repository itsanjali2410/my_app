import pandas as pd
df= pd.read_csv("V5.csv")
# df = pd.read_csv("V5.csv", na_values=["?"]) #values are for plural this is also matters in pandas
# print(df.head())
# print(df.isnull().sum())
# df = pd.read_csv("")
# print(f"Total missing values in dataset: {df.isnull().sum().sum()}")
df["Estimated Value"] = df["Estimated Value"].fillna(df["Estimated Value"].median())
df["carpet_area"] = df["carpet_area"].fillna(df["carpet_area"].mean())
df["Locality"] = df["Locality"].fillna(df["Locality"].mode()[0]) #For categorical columns (like Locality and Property), use the most frequent value (mode)
df["Property"] = df["Property"].fillna(df["Property"].mode()[0])
# print(f"Total missing values in dataset: {df.isnull().sum().sum()}")
print(f"value : {df.iloc[692,0]}") #to find position[row_value, column_value]
print(f"value : {df.iloc[546,7]}")
print(f"uniques_values:{df.apply(pd.Series.unique)}")  #to find uniques values in the all file
print(f"unique value in a column: {df['Locality'].unique()}")
# List the features that have missing values
# missing_values = df.isnull().sum()
# missing_features = missing_values[missing_values > 0]
# print(missing_features)

df_cleaned = df.dropna(thresh=df.shape[1] - 2)

# Count the number of remaining rows
remaining_rows = df_cleaned.shape[0]
print(f"Number of samples remaining: {remaining_rows}")

# Drop all rows with any missing values
df_missing = df.dropna()

# Count the number of remaining rows
remaining_rows = df_missing.shape[0]
print(f"Number of samples remaining: {remaining_rows}")


#graded assignment 1.2
#to get evenrows
even_rows = df.iloc[::2]
# value = even_rows.iloc[0,3]
print(f"{even_rows.iloc[0,3]}")
print(f"{even_rows.iloc[332,3]}")

#to get odd rows
odd_rows = df.iloc[1::2]
print(f"{odd_rows.iloc[332,3]}")
print(f"{odd_rows.iloc[100,5]}")

#select rows and rows using iloc
even_rows_col = df.iloc[::2,::2]
print(f"{even_rows_col.iloc[255,3]}")

# Sort the 'Year' column in descending order and get the six most recent years
most_recent_years = df['Year'].dropna().unique()
most_recent_years = sorted(most_recent_years, reverse=True)[:6]

# Filter the rows for these six most recent years
filtered_df = df[df['Year'].isin(most_recent_years)]

# Get the number of rows (samples) in the filtered dataframe
num_samples = filtered_df.shape[0]

print(f"Number of samples (rows) in the six most recent years: {num_samples}")

#The result will be the count of rows where num_rooms equals 3 and num_bathrooms equals 3.
#AND Function
count = df[(df['num_rooms'] == 3) & (df['num_bathrooms'] == 3)].shape[0]
print(count)

#OR function
count = df[(df['num_rooms'] == 3) | (df['num_bathrooms'] == 3)].shape[0]
print(count)


average_sale_price_by_locality = df.groupby('Locality')['Sale Price'].mean()

# Find the locality with the highest average sale price
highest_avg_sale_price_locality = average_sale_price_by_locality.idxmax()
highest_avg_sale_price = average_sale_price_by_locality.max()

print(f"The locality with the highest average Sale Price is {highest_avg_sale_price_locality} with an average Sale Price of {highest_avg_sale_price}")

# Filter the dataset for Year 2022, Locality 'Greenwich', num_rooms == 3, and Face as 'North' or 'East'
filtered_df = df[(df['Year'] == 2022) & 
                 (df['Locality'] == 'Greenwich') & 
                 (df['num_rooms'] == 3) & 
                 (df['Face'].isin(['North', 'East']))]

# Get the number of rows (houses) that satisfy these conditions
num_houses = filtered_df.shape[0]

print(f"Number of houses located in Greenwich in 2022 with exactly 3 rooms and facing North or East: {num_houses}")

 
# Convert 'Date' column to datetime if it's not already
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter the dataset for rows where the month is August (month == 8)
august_rows = df[df['Date'].dt.month == 8]

# Get the number of rows corresponding to August
num_august_rows = august_rows.shape[0]

print(f"Number of samples corresponding to the month of August across all years: {num_august_rows}")

import pandas as pd
import numpy as np

# 1. Load the CSV dataset
file_path = 'cleaned_customer_data.csv'
df = pd.read_csv(file_path)

print("--- Initial Data Summary ---")
print(f"Initial Shape: {df.shape}")
print("\nMissing values per column:")
print(df.isnull().sum())

# 2. Check and remove duplicate rows
duplicates_count = df.duplicated().sum()
print(f"\nDuplicate rows found: {duplicates_count}")

df = df.drop_duplicates().reset_index(drop=True)

# 3. Handle Missing Values
# Fill numeric missing values (Age, Salary) with their median
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

# Fill categorical missing values (City) with 'Unknown' or Mode
df['City'] = df['City'].fillna('Unknown')

# 4. Standardize Text Formatting
# Standardize column names (lowercase with underscores)
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Strip trailing spaces and standardize text in string columns
text_columns = ['first_name', 'last_name',
                'city', 'subscription_type', 'status']
for col in text_columns:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip().str.title()

# 5. Format Date Column
if 'join_date' in df.columns:
    df['join_date'] = pd.to_datetime(df['join_date'])

# 6. Verify Cleaned Data
print("\n--- Cleaned Data Summary ---")
print(f"Final Shape: {df.shape}")
print("\nMissing values remaining:")
print(df.isnull().sum())
print("\nCleaned Data Sample:")
print(df.head())

# 7. Save the Cleaned Dataset
df.to_csv('cleaned_customer_data.csv', index=False)
print("\nCleaned dataset successfully saved to 'cleaned_customer_data.csv'")

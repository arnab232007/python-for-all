import pandas as pd
import numpy as np

# 1. Create a mock dataset with missing values
# We use np.nan (Not a Number) to represent empty/blank cells
data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Desk'],
    'Price': [1200, 25, np.nan, 75, np.nan],       # 2 missing prices
    'In_Stock': [15, np.nan, 8, np.nan, 3],        # 2 missing stock counts
    'Rating': [4.5, 4.2, 4.0, np.nan, 4.8]         # 1 missing rating
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

print("=== 1. THE ORIGINAL DATAFRAME ===")
print(df)
print("\n" + "="*40 + "\n")

print("=== 2. WHAT df.isnull() SEES ===")
# This turns everything into True/False values
print(df.isnull())
print("\n" + "="*40 + "\n")

print("=== 3. FINAL OUTPUT OF df.isnull().sum() ===")
# This counts the 'True' values column by column
print(df.isnull().sum())
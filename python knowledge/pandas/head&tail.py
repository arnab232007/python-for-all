import pandas as pd

# 1. Create a mock dataset (dictionary format)
data = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'Marketing', 'Finance', 'HR', 'Marketing', 'IT', 'Finance'],
    'Salary': [65000, 85000, 95000, 70000, 62000, 91000, 68000, 60000, 105000, 88000],
    'Remote': [True, False, False, True, True, False, True, False, False, True]
}

# 2. Convert the dictionary into a Pandas DataFrame (df)
df = pd.DataFrame(data)

# =====================================================================
# INSPECTION DEMO
# =====================================================================

print("--- 1. DEFAULT HEAD (First 5 Rows) ---")
# If empty, defaults to 5 rows
print(df.head()) 
print("\n" + "="*50 + "\n")


print("--- 2. CUSTOM HEAD (First 3 Rows) ---")
# Specify exactly how many rows you want
print(df.head(3)) 
print("\n" + "="*50 + "\n")


print("--- 3. DEFAULT TAIL (Last 5 Rows) ---")
# If empty, defaults to 5 rows
print(df.tail()) 
print("\n" + "="*50 + "\n")


print("--- 4. CUSTOM TAIL (Last 2 Rows) ---")
# Great for checking the very end of your data
print(df.tail(2)) 
print("\n" + "="*50 + "\n")


print("--- BONUS: QUICK DATA INFO ---")
# Bonus: df.info() shows you the data types and if any data is missing (NaN)
print(df.info())
print("\n")
print(df.describe())  # Quick stats for numeric columns
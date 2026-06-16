import pandas as pd 
data = {
    "roles" : ["IT", "HR", "IT", "Finance","HR"],
    "salary" : [50000, 60000, 55000, 70000, 65000]
}

DF = pd.DataFrame(data)
print("Original DataFrame :\n", DF) 
print("\n" + "="*50 + "\n")
print(DF.groupby("roles")["salary"].sum())
print("\n" + "="*50 + "\n")
print(DF.groupby("roles")["salary"].mean())

print(DF.sort_values("salary", ascending=False))
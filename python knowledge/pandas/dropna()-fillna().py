import pandas as py 
df = {
    "name": ["A", "B", "C", "D"],
    "age": [25, 30, 35, 40],    
    "marks": [90, 95, 85, 80],
    "ID": [1, 0, 3, 4]
}
DF =py.DataFrame(df)
print("original data :", DF)

print("DataFrame after dropping column 'ID' :\n", DF.drop("ID", axis=1)) 

print(DF.fillna(0))
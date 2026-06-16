import pandas as py 
data = {
    "name": ["A", "B", "C", "D"],
    "age": [25, 30, 35, 40],
    "marks": [90, 95, 85, 80],
    "ID": [1, 2, 3, 4]
}

DF = py.DataFrame(data)
print("original data :", DF)

print("DataFrame after dropping column 'ID' :\n", DF.drop("ID", axis=1))

print("dataframe marks :\n", DF[DF["marks"] >= 90]) 

print("dataframe with age > 30 :\n", DF[(DF["age"] > 30) & (DF["marks"] > 85)])
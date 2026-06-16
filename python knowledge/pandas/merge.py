import pandas as py 
data1 = {
    "name": ["A", "B", "C", "D"],
    "age": [20, 25, 30, 35] ,
    "id": [1, 2, 3, 4]
}
df1 = py.DataFrame(data1)

data2 = {
    "name": ["E", "F", "G", "H"],
    "age": [40, 45, 50, 55],
    "id": [4, 6, 7, 8]
}
df2 = py.DataFrame(data2)

print("dataframe 1 :\n", df1)
print("\n" + "="*50 + "\n")
print("dataframe 2 :\n", df2)
print("\n" + "="*50 + "\n")
print("concatenated dataframe :\n", py.concat([df1, df2]))
print("\n" + "="*50 + "\n")
print("merged dataframe :\n", py.merge(df1, df2, on="id"))
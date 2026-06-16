import pandas as py 
s = {
    "name" : ["Arnab","Rahul"],
    "age" : [25, 30],
    "marks" : [90, 95]
}

d = py.DataFrame(s)
print("Panda DataFrame :\n", d)
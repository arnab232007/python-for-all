a = (1,4,9,16,25,36,49,64,81,100)
i = 0 
n = int(input("enter the number:"))

while i<len(a):
    if n == a[i]:
        print("found at i =",i)
        break
    i +=1
else:
    print("not found ") # if the element is not found it will print not found


a = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i < len(a):
    if a[i] == 5:
        break
    print(a[i])
    i += 1 

b = [1,2,3,4,5,6,7,8,9,10,11] 
j = 0
while j < len(b):
    if b[j] == 5:
        j+=1
        continue 
else:
    print(b[j])
    j+=1
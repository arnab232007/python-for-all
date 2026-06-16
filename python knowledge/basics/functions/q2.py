a = ["kolkata","mumbai","delhi","chennai","bangalore"]
def func(list):
    i = 0
    while i < len(list):
        print(list[i],end=" ")
        i+=1

func(a) 
print("\n")
def func2(list): 
    for items in list:
        print(items, end=" ")

b = [1,2,3,4,5,6,7,8,9,10]

func2(b)
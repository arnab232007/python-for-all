a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
c = int(input("enter the value of c:"))

if(a>b and a>c):
    print("a is greatest")
elif(b>a and b>c):
    print("b is greatest")
else:
    print("c is greatest")
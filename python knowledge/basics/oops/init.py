class student :
    def __init__(self,name,age):
        self.name = name # self is used to refer to the current object 
        self.age = age

s1 = student("arnab",19)
print(s1.name)
print(s1.age)
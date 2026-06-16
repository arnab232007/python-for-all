class student : 
    def __init__(self , name ,marks):
        self.name = name 
        self.marks=marks 
    def avg(self):
        sum = 0 
        for val in self.marks :
            sum+=val
        print("hi", self.name , "your avg marks is :",sum/3)


s1 = student("arhaan" , [89,54,87])
print(s1.marks)

s1.avg()


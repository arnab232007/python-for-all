def fact(n):
    fac = 1 
    for i in range(1,n+1) : # factorial problem using function 
        fac *=i
        i+=1
    return fac

print(fact(5)) # 5*4*3*2*1 = 120 

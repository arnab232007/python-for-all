a = {1,2,3,4,5,5,5,8,6,7,8,9,10}
a.add(11) 
print(a)  # adds the element to the set 

a.remove(11) 
print(a)  # removes the element from the set 

a.discard(11) 
print(a)  # removes the element from the set 

a.pop() 
print(a)  # removes the element from the set 

a.clear() 
print(a)  # removes all the elements from the set 

b = {1,2,3,4,5,"hhhh",7,8,9,10}
ff = a.union(b) 
print(ff)  # adds all the elements from the set 

a.intersection(b) 
print(a)  # adds all the elements from the set 

a.copy() 
print(a)  # adds all the elements from the set 

a.update(b) 
print(a)  # adds all the elements from the set  
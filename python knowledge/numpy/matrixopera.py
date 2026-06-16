import numpy as np 
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[7,8,9],[10,11,12],[13,14,15]]) 
print(np.dot(a,b))
print(np.transpose(a))
print(np.linalg.inv(a))
print(np.linalg.det(a)) 


ac = np.array([[1,2],
              [3,4]])

bc = np.array([[5,6],
              [7,8]])

print(np.dot(ac,bc))
print(ac.T)
print(np.linalg.det(ac))
print(np.linalg.inv(ac))
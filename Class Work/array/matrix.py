import numpy as np

arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1)

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2)

print("multiplying \n")
m1 = np.dot(arr1,arr2)
print(m1)

print("adding \n")
a1 = print(np.add(arr1,arr2))

print("subtracting \n")
s1 = print(np.subtract(arr1,arr2))

t1 = arr1.T
print(f"transposed \n {t1}")
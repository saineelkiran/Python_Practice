from numpy import *

arr =array([4,5,6])
arr=arr+5


arr1 = array([10,20,30,40])
arr2=array([5,10,15,20])
arr3=arr1+arr2

arr4=arr3.copy()
arr3[2]=44
print(arr3)
print(arr4)

print(id(arr3))
print(id(arr4))
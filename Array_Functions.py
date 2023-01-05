from numpy import *

arr = array([45, 35, 27, 43, 23, 89, 65], float)
print(arr)
print("Dtype o/p :" + str(arr.dtype)+"\n")

#ls = linspace([1,2,3,4,5],8)
#print(ls)

log_sp= logspace(0,50,5)
print('%2f' %log_sp[2])

arnge = arange(1,25,5)
print("Arange o/p "+str(arnge))

zer= zeros(10,int)
print(zer)

on=ones(10,int)
print(on)
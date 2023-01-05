from array import *
#from numpy import *
arr =array('i',[])
x= int(input("Enter the len Of Array : "))

for j in range(x):
    p=int(input("Enter the value number " + str(j+1) +" "))
    arr.append(p)

print(arr)

s = int(input("Enter the value to be searched : "))
k=0
for e in arr:
    if e==s:
        print("Index of the number " + str(s) +" is " + str(k))
        break
    k+=1
else:
    print("Number not found in Array")
print ("Output using index function : "+str(arr.index(s)))


#-------------------------------------------------------------------------------------------------------------
"""
val = array('f', [2.5, 6, 8, 4, 9.2])
print("Buffer Info (Memory code, length of array) "+str(val.buffer_info()))

new_val = array(val.typecode,(a*a for a in val))

for i in new_val:
    print(i)
"""
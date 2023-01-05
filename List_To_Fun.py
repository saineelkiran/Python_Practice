from array import *

lst = int(input("Enter length of Array : "))
xyz =array("i",[])
for j in range(lst):
    y=int(input("Enter the Value number : " + str(j+1)+" "))
    xyz.append(y)

def count(xyz):
    even=0
    odd=0
    for i in xyz:
        if(i%2==0):
            even+=1
        else:
            odd+=1
    return even,odd

even,odd = count(xyz)
print("Even : " + str(even)+" Odd : " +str(+odd))
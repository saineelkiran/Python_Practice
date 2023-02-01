from array import *
lst = array('i', [1, 2, 3, 4, 7, 0, 8, 4])
#p=lst[0]
max=1
for i in range (len(lst)-1 ):
    for j in range (i+1, len(lst)):
        prod = lst[i] * lst[j]
        if prod >max:
           max= prod
           p= lst[i]
           q= lst[j]


print("Numbers are \n"+str(p)+","+str(q))
print("Product is \n"+str(max))


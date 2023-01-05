from functools import reduce

lst =[2,4,6,7,9,10,11,12]

even =list(filter(lambda x : x%2==0,lst))
print(even)
doub= list(map(lambda p : p*2,even))
print(doub)
red= reduce(lambda x,y:x+y,doub)
print(red)
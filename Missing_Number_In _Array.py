#Find missing number between 10 to 20
from array import *
def miss(nums):
    y=len(nums)
    z=nums[0]+y+1
    return sum(range(nums[0],z)) - sum (list(nums))

ar = array("i", [25,26,28,29,30,31,32,33,34,35])
print("Original Array is ")
for i in range(len(ar)):
    print(ar[i], end=" ")

print ("\nThe missing element from the above array is : \n", miss(ar))

import math
num = int(input("Enter number to check if it is prime or not "))
#If u can check the square root of a number and check the values until then , we can conclude it is not prime

for i in range (2,num):
    if(num%i==0):
        print("The number " + str(num) + " is not prime")
        break
else:
    print("The number " + str(num) + " is prime")


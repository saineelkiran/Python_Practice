#Candy Machine
Available = 5
x = int(input("Please enter the number of Chocolates you need "))
i=1
while (i<=x):
        if x>Available:
            print("Required Quantity Not Available . Select  " +str(Available) + " or less quantity")
            break
        print("chocolate ", end="")
        i+=1
        #Available= Available-x
        #print("Inventory after transaction is " + str(Available))

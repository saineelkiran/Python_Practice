def fact(n):
    z=1
    for i in range(1,n+1):
        z=z*i
        i=i+1
    return (z)

result= fact(int(input("Enter number to find factorial : ")))
print("Factorial of number is ",result)

def fib(n):
    sum = 0
    x=0
    y = 1
    if(n<=0):
        print("Cannot get fibinocci series for negative numbers or zero")
    else:
        for i in range(n):
            print(x)
            sum=x+y
            if sum >100:
                print("Value greater than 100")
                break
            y=x
            x=sum

fib(int(input(" Enter the fibinaci number please  : ")))
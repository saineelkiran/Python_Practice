x=0
y=1
sum=0
z=0
count =int(input("count of fabinacci series you require ? "))
while (z<=count):
    if z>15:
        print("too large value")
        break
    sum=x+y
    print(x,",", end="")
    x=y
    y=sum
    z+=1

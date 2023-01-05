list =[23,54,78,35,90]

for num in list:
    if num%7==0:
        print(str(num) + " divisible by 7")
        break
else:
    print("No other num divisible by 7")

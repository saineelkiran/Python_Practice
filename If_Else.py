
age = int(input("Please enter the age "))

if (age >12):
    if age<18:
        print("You are minor!! Hence your ticket price is 2000 INR")
    elif age>=18 and age <=35:
        print("For youth, ticket price is set to 5000 INR")
    else:
        print("Your ticket price is set to 7000 INR")
else:
    print("You are too young to watch a match! Ticket not allowed")


x= int(input("Enter the numerator value : "))
y= int(input("Enter the denominator value : "))

try:
    print("Execution of try block started")
    print(x/y)

except ZeroDivisionError as e:
    print("Please dont divide the number by zero, give a valid number for denominator - ", e)

except ValueError as e:
    print("please do not give non-numerical values - ",e)

except Exception as e:
    print(e)

finally:
    print("Execution of try block ended")
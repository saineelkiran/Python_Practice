# Python dictionary is a container of the unordered set of objects like lists.
# The objects are surrounded by curly braces { }.
# The items in a dictionary are a comma-separated list of key:value pairs where keys and values are Python data type.

# dic={'first_name':'Sai Neel', 'last_name': 'Chittajallu', 'State':'Telangana','Country':'India'}
# print(dic['State'])
# print("\n")
# print(dic)


def mult(*args):
    result =1
    for i in args:
        result=result*i
    return result

print(mult(1,2,5,8,4,5,8,9,10))
a=20
b=7
c=6

def new():
    global a
    a=5
    x=globals()['a']
    print(id(a))
    print("Local Value inside function : ",a)
    print(id(x))
    # globals()['a']=99
new()

print("Global Value : ", a)
print(id(a))
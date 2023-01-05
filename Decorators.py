def div(a,b):
    print (a/b)

def smart_div(fun):
    def inner(x,y):
        if x<y:
            (x,y)=(y,x)
        return fun(x,y)
    return inner

div=smart_div(div)
div(4,8)
pos=-1
def search(list,n):
    for i in list:
        global pos
        pos = pos + 1
        if i==n:
            return True
    else:
        return False

n=45
list =[25,56,75,45,12,98,39,42,86,74]
if search(list,n):
    print("Search Element - Found at the position : ", pos+1)
else:
    print("Search Element -  Not Found")
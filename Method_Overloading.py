class student:
    def __int__(self,p1,p2):
        self.p1=p1
        self.p2=p2

    def sum(self,a=None,b=None,c=None):
        if(a!=None and b!=None and c!=None):
            s=a+b+c
        elif(a!=None and b!=None):
            s=a+b
        else:
            s=a
        return s

y=student()
print(y.sum(90,9))
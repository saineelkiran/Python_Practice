from math import *
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3

    def __gt__(self, other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False

c1=student(44,45)
c2=student(45,50)
c3=c1+c2
print(c3.m2)
if(c1>c2):
    print("C1 has better marks")
else:
    print("C2 has better marks")

print(id(c1))
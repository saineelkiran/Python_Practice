class A:
    def feature1(self):
        print("feature 1 from class A")
#Single level Inheritance
class B(A):
    def feature2(self):
        print("feature 2 from class B")

#Multilevel Inheritance
class C(B):
    def feature3(self):
        print("feature 3 from class C")

class D():
    def feature4(self):
        print("feature 4 from class D")
# Multiple Inheritance
class E(A,D):
    def feature5(self):
        print("feature 5 from class E")

a=A()
b=B()
c=C()
d=D()
e=E()
a.feature1()
c.feature2()
c.feature3()
d.feature4()
e.feature5()


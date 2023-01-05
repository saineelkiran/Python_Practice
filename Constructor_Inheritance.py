class A:
    def __init__(self):
        print("This is Init in class A")
    def feature1(self):
        print("This is feature1 in Class A")

class B:
    def __init__(self):
        super().__init__()
        print("This is init in class B")
    def feature2(self):
        print("This is feature2 in Class B")
    def feature1(self):
        print("This is feature1 in Class B")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("This is init in class C")
       
    def feat(self):
        super().feature2()
#Method Resolution Order(Left to Right)
c=C()
b1=B()
c.__init__()
c.feat()

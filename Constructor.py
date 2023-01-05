class computer:
    def __init__(self):
        self.name ="Sai Neel"
        self.age= 32

    def update(self):
        self.age=2

    def compare(self,other):
        if(self.age == other.age):
            return True
        else:
            return False

c1=computer()
c2=computer()

c2.update()

if c1.compare(c2):
    print("They are Same")

else:
    print("They are different")

print("Age Of C1 is ",c1.age)
print("Age Of C2 is ",c2.age)


print("ID Of C1",id(c1))
print("ID Of C2",id(c2))
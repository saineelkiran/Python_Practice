from math import *


class student:
    school = 'Blue Rays Institution'

    def __init__(self, math, phy, chem):
        self.math = math
        self.phy = phy
        self.chem = chem

    def avg(self):
        return (self.math + self.phy + self.chem) / 3

    # Class method
    @classmethod
    def get_school(cls):
        return cls.school
    @staticmethod
    def info():
        print("This is an example for Static Method")


s1 = student(76, 79, 80)
s2 = student(90, 80, 85)

print("Average marks of C2 is ",ceil(s2.avg()))
print(student.get_school())
student.info()


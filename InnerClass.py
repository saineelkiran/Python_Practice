class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class laptop:
        def __init__(self):
                self.brand="ASUS"
                self.ram="8 GB"
                self.ssd="500 GB"

        def show(self):
            print(self.brand,self.ram,self.ssd)

s1=student("Sai Neel",8)
s2=student("Kiran",9)

s1.show()
# student.laptop().show()
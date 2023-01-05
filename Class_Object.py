class computer:
    def __init__(self,CPU,RAM):
        self.CPU=CPU
        self.RAM=RAM

    def config(self):
        print(self.CPU,self.RAM)

comp1=computer("I5","500GB")
comp2=computer("AMD ryzen 5","256GB")
comp1.config()
comp2.config()
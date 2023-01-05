class Pycharm:
    def execute(self):
        print("Debugging")
        print("Running")

class Laptop :
    def code(self,ide):
        ide.execute()

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")


ide=MyEditor()
#ide=Pycharm()
lap1 =Laptop()
lap1.code(ide)


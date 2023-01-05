from threading import *
from time import *
class hello(Thread):
    def run(self):
        for i in range(5):
            print('Hello')
            sleep(0.5)

class hi(Thread):
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(0.5)

h1=hello()
h2=hi()
h1.start()
sleep(0.1)
h2.start()

h1.join()
h2.join()
print("Completed")
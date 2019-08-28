# thread is a light weight process
# at one point you can run multiple applications
from time import sleep
from threading import *


class Hello(Thread):
    def run(self):
        for i in range(4):
            print("Hello")
            sleep(1)

class Hi(Thread):

    def run(self):
        for i in range(4):
            print("Hi")
            sleep(1)

a=Hello()
b=Hi()

a.start()
sleep(.2)
b.start()

a.join()
b.join()
print("bye")
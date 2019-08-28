class computer:

# __init__ to initialise the variables    it is special method it is like constructor

# how many objects created based on that the init method is called automatically

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        # print("called init")


    def config(self):
        print("i5 16GB, 1TB")
        print("config is: ",self.cpu,self.ram)

com1=computer("i5",16)
com2=computer("Rysen 3",32)
# 1 way of calling obects
# computer.config(com1)
# computer.config(com2)

# 2 way of calling obects
com1.config()
com2.config()
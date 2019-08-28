class Hello:
    def __init__(self):
        print("The __init__")

hello=Hello()


# Multiple Constructor Concept
'''  
class Bye:
    def __init__(self):                         # this init method is overwritten                         
        pass
    def __init__(self,name):                    # this init method taken into consideration
        pass

tata1=Bye("Ratan")

'''
class Grow:
    # def __init__(self,name="Max"):        # or
    # def __init__(self,*args):
    def __init__(self, *args,**kwargs):
        pass

g1=Grow()
g2=Grow("Hi",name="Ajit")


# 4 questions no need to pass all variables pass to init method some are static value also like age

class Next:
    def __init__(self,name):
        self.name=name
        self.age=10
        print("The __init__")


n=Next("John")
print(n.name)
print(n.age)
'''
class TestClass:
    def __init__(self):
        print("constructor")

    def __del__(self):
        print("destructor")

if __name__=="__main__":
    t1=TestClass()
    del t1
'''

class Edureka:
    def __init__(self):
        self.__pri=("Iam Private")
        self._pro=("Iam Protected")
        self.pub=("Iam Public Method")

    @classmethod
    def mycustomConstructor(cls,employee_strength):
        cls.employee_strength=employee_strength

    def __del__(self):
        self.___pro=None
        print("Object will be deleted")

    def __privatemethod(self):
        print("In Private")

default_ab=Edureka()
ob=Edureka.mycustomConstructor(300)



# ob.__Edureka__privatemethod()
# print(ob.__Edureka__pri)
# ob.__Edureka__.privatemethod()
# print(ob.__Edureka__pri)
'''
class Attributes:
'''

'''
    empcount=0

print("Attributes.__dict__",Attributes.__dict__)        # __dict__ is builtin sttribute in python.
print("Name:",Attributes.__name__)
print("Attributes:",Attributes.__doc__)
print("Attributes Module",Attributes.__module__)
print("Edureka base:",Attributes.__bases__)

'''


class Demo():
    def __init__(self):
        self.pub="Iam Public"
        self._pro="Iam Protected"
        self.__pri="Iam Private"

    def __privatemethod(self):
        print("In private Method")

d=Demo()
print(d.pub)
print(d._pro)
# print(d.__pri)          # we cannot access thos private because this is accessible only in class only.
# d.__private_method()
d._Demo__privatemethod()
print(d._Demo__pri)

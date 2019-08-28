class getset:
    def __init__(self,name):
        self.name=name

    def getvalue(self):
        return self.name.lower()

    def setvalue(self,name):
        self.name=name

o=getset("Manoj")
print(o.getvalue())
# o.setvalue="Harsha"
o.setvalue("Jambookam")
print(o.getvalue())

from math import sqrt
print(dir())
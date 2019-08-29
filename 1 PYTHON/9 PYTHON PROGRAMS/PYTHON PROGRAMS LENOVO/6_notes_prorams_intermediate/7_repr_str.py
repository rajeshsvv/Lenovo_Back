class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+'@gmail.com'

    def fullname(self):
        return "{}.{}".format(self.first,self.last)

    def apply_rasie(self):
        self.pay=int(self.pay*1.04)

    def raise_amt(cls, amount):
        pass

    def __repr__(self):
        return "Employee({}.{}.{})".format(self.first,self.last,self.pay)

    def __str__(self):
        return "{}.{}".format(self.fullname(),self.email)

emp1=Employee("Corey","Schafer",60000)
emp2=Employee("Test","User",6000)

print(emp1.__repr__())
print(emp2.__str__())



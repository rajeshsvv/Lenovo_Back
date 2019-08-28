# property decorators
# using getter and setter properties by python decorators
# python property decorator allows us to define a method but we can access it like as a attribute


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Deleted Name!")
        self.first = None
        self.last = None

    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)


emp_1 = Employee("John", "Smith", 25000)
emp_2 = Employee("Sarah", "Dongly", 25000)


emp_1.first = "Jim"
emp_1.fullname = "Corey Schafer"
emp_1.fullname = "Code Camp"
emp_1.last = "Camp"
print(emp_1.last)
# before it is attribute so no need to use () but now it is method so thats why we use () to get actual result before @property
print(emp_2.email)

# after decorating the email method with @property we dont use () because it access like attributes.for attributes no need ()
print(emp_1.email)
print(emp_1.fullname)

# del emp_1.fullname
print(emp_1.first)

# python class inheritance

"""
inheritance allows us to inherits attributes and methods from parent class

python whisky library it is very popular used in different projects

"""


class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):  # inherits the employee class so all the attributes are inherited to Developer class
    raise_amount = 1.10

    # here i extend the functionality of Developer class with add an attribute of programming language
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # both we can use but super is most commonly use in case of multiple inheritance
        # Employee.__init__(first,last,pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)  # both we can use but super is most commonly use in case of multiple inheritance
    # Employee.__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname)


emp_1 = Employee("Corey", "Schafer", 20000)
emp_2 = Employee("Test", "User", 30000)

dev_1 = Developer("Andrew", "Kelly", 20000, "Python")
dev_2 = Developer("Skott", "Jennifer", 50000, "R")

mgr_1 = Manager("Sue", "Smith", 25000, [dev_1])

# mgr_1.add_emp(dev_2)
# mgr_1.add_emp(dev_1)
# mgr_1.rem_emp(dev_1)
# mgr_1.print_emps()

# print(help(Developer))  # for getting the details about Developer class got it
# print(emp_1.email)
# print(emp_2.email)
# print(dev_1.first)
# print(dev_2.email)

# print(emp_1.email)
# print(emp_2.first)
# print(dev_1.prog_lang)
# print(dev_2.prog_lang)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)


"""
python has two built in functions are called 
is instance and is sublcass
isinstance:it will tell us if an object is an instance of an class
issubclass:it will tell us if a class is a subclass of another class
"""

print(isinstance(mgr_1, Employee))
print(isinstance(dev_1, Employee))
print(isinstance(mgr_1, Developer))
print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))
print(issubclass(Manager, Developer))

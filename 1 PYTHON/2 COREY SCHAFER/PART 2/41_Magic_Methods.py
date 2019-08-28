# Magic Methods in inheritance OOPS concepts
"""
by using magic methods we can able to change the built in behaviour and operations
magic methods are defined by double underscores lot of people are called dunder
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

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{}:{}".format(self.fullname(), self.email)

    def __add__(self, other):  # this is for two employees salaries
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


"""
# these repr or str are inplicitly called these fix the problem of vague(unclear) employee object information
REPR is met to be an unambiguous representation of the object and should be used for debugging and logging things like that
STR is meant to be more of readable representation of an object and is meant to be used as a display to the end user
"""


emp_1 = Employee("Corey", "Schafer", 20000)
emp_2 = Employee("Test", "User", 30000)

# repr(emp_1)
# str(emp_1)
# print(emp_1)

print(repr(emp_1))
print(str(emp_1))

# print(emp_1.__repr__)
# print(emp_1.__str__)
# print(emp_1.__repr__())
# print(emp_1.__str__())

# dunders are on arithmatic operators

# print(1 + 2)
# print(int.__add__(1, 2))
# print("a" + "b")
# print(str.__add__('a', 'b'))

# print(emp_1 + emp_2)
# print(len("test"))  # background dunder metod will calling otherwise check down once
# print("test".__len__())
# print(len(emp_1))

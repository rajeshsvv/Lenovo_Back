# regular methods vs class methods vs static methods
"""
@regular methods:
regular methods in class automatically takes the instance as the first arguments and by convention we were
calling this self.so if a regular method automatically takes an instance as the first argument then how can we change this so that it
instead automatically takes the class as first argument now to do that we are using class methods and
to turn regular method into class method its easy as adding a decorator to the top called class method like this @classmethod

@classmethod:
it basically alters the functionality of the method where we now receive the class as our first argument instead of instance
common convention for regular method we call instance variable as self.
common convention for class method we call instance variable as cls.
class methods which can also be used as alternate constructors
@static methods:
when working with the classes regular methods automatically pass the instance as the first argument and we call that self.
and 						  class methods automatically pass the class as the first argument and we call that cls.
							  satic methods dont pass anything automatically they dont pass instance or class so they really behave
							  static methods does not take instance or class as the first argument
							  just like a regular functions except we include them in our class because they have some logical connection
							  with the class
							  static methods which dont operate on the instance or the class
# static methods example
for example a simple function that take a date and return whether or not that was a work day
so this has a logical connection to our employee class but it does not actually depend upon any class variable or specific instance
so we create static method here it is same as class method to create the static method use like #staticmethod
static methods does not take instance or class as the first argument
so that we can pass arguments we are working right now
in python dates have weekday methods
monday=0 sunday=6 and all the other days in between them
"""


class Employee:

    raise_amount = 3.52  # these type of declaration of variables we called as class variable
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "first" + "." + "last" + "@company.com"
        Employee.num_of_emps += 1

    # method creation for diplay full name
    def fullname(self):
        return ("{} {}".format(self.first, self.last))

     # method creation for class variable example
    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)			#this is through class variable
        self.pay = int(self.pay * self.raise_amount) 			    # this is through instance variable

    @classmethod
    def set_raise_amnt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)    	# why i use return here because it will create new employee object here so to return the new object

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False  # it does not hit condition thats why it is false.it is weekend
        return True  # it does hit condition thats why it is True.it is weekday


import datetime

today_date = datetime.date(2018, 2, 10)
print(Employee.is_workday(today_date))


print(Employee.num_of_emps)  # before instantiation of employees it becomes 0
emp1 = Employee("Corey", "Schafer", 30000)
emp2 = Employee("test", "user", 10000)
print(Employee.num_of_emps)  # after instantiation of employees it becomes 2

# Employee.set_raise_amnt(3.598)
# # emp1.set_raise_amnt(3.589)  # you can run class methods from instances but this is not make sense corey does not prefer this
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)


# class methods example
# emp_str_1 = "John-Doe-60000"
# emp_str_2 = "Corey-Schafer-70000"
# emp_str_3 = "Code-Camp-30000"

# # this is work but this is hard coded so instead of that we create one method to common the things
# # first, last, pay = emp_str_1.split("-")
# # new_emp1 = Employee(first, last, pay)
# # print(new_emp1.pay)

# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.pay)

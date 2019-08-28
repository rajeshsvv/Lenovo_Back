# class variables that are shared among all instances of a class
# instance variables contain data that is unique to each instance


class Employee:

    raise_amount = 2.36  # class variable
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
        # self.pay = int(self.pay * Employee.raise_amount)          #this is through class variable
        self.pay = int(self.pay * self.raise_amount)                # this is through instance variable


print(Employee.num_of_emps)  # before instantiation of employees it becomes 0
emp1 = Employee("Corey", "Schafer", 30000)
emp2 = Employee("test", "user", 10000)
emp3 = Employee("Jony", "Walker", 10000)
print(Employee.num_of_emps)  # after instantiation of employees it becomes 3

# print(emp1.first)
# print(emp2.email)

# print(emp1.fullname())
# print(Employee.fullname(emp2))  # call by using class but we need to mention which instance is called

# print(emp2.pay)
# emp2.apply_raise()
# print(emp2.pay)
print(emp1.__dict__)            # __dict__ useful for what the attributes it contains this is instance level
print(Employee.__dict__)        # this is class level what the attributes it have

# Employee.raise_amount = 1.05
# emp1.raise_amount = 2.36
# print(emp1.__dict__)
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)

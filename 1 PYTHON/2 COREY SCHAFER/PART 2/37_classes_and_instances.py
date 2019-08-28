# classes and instances
# classes logically group our data and function in a way thats easy to reuse
# when i say data and functions are associated with a specific class we call those attributes and methods
# when i say methods i mean function associated with a class.
# class is a blueprint for creating instances.

# instance variables vs class variables.
# instance variables contain data that is unique to each instance
# class variables that are shared among all instances of a class

# GENERAL WAY
# class Employee:
#     pass


# emp1 = Employee()
# emp2 = Employee()

# emp1.first = "Corey"
# emp1.last = "Schafer"
# emp1.mail = "Corey.Schafer#gmail.com"
# emp1.salary = 30000

# emp2.first = "test"
# emp2.last = "mail"
# emp2.mail = "test.mail#gmail.com"
# emp2.salary = 30000
# print(emp1.first)
# print(emp2.last)


# INIT way
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    # method creation for diplay full name
    def fullname(self):
        return ("{} {}".format(self.first, self.last))


emp1 = Employee("Corey", "Schafer", 30000)
emp2 = Employee("test", "user", "10000")

print(emp1.first)
print(emp1.email)
print(emp2.email)
print(emp1.fullname())
print(Employee.fullname(emp2))  # call by using class but we need to mention which instance is called
# to print full name but this is lot of typoes so may be we will get an error so for this we create an method
#print("{} {}".format(emp1.first, emp1.last))

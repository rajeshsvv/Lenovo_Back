class Salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus

    def annual_salary(self):
        return (self.pay*12)+self.bonus

class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.obj_salary=salary

    def total_salary(self):
        print(self.obj_salary.annual_salary())
        # return self.obj_salary.annual_salary()


salary=Salary(25000,5000)
emp=Employee("Alex",25,salary)
emp.total_salary()                # if u use print in function call the function by this way.
# print(emp.total_salary())     # if u use return statement in function call the function by this way


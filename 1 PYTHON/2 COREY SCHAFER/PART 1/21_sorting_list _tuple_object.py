# sort lists  dictionaries and objects also

# sort on Lists
"""
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

# sort_li = sorted(li)
sort_li = sorted(li, reverse=True)  # sorted function returns a new sorted list so thats why we can set to new variable.this function has more flexibility
print("Sorted Variable:\t", sort_li)  # \t for equal space

li.sort()  # sort method just sorts the lists and then plays returns none
li.sort(reverse=True)
print("Original variable:\t", li)
"""

# sort on tuples there is no sort method on tuple got it
"""
tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)
print(s_tup)
"""

# sort on dictionaries there is no sort method on tuple got it
"""
di = {"name": "Corey", "job": "Programming", "age": None, "os": "Mac"}
s_di = sorted(di)
print("Dict:\t", s_di)
"""

li = [-6, -5, -4, 3, 2, 1]
print(li)

li = [-6, -5, -4, 3, 2, 1]
# s_li = sorted(li)
s_li = sorted(li, key=abs)  # key parameter is extremely useful when sorting objects with named attributes
print(s_li)


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)


from operator import attrgetter


e1 = Employee("Carl", 37, 60000)
e2 = Employee("Sarah", 28, 45000)
e3 = Employee("John", 26, 30000)

employees = [e1, e2, e3]


# def e_sort(emp):
# return emp.name
# return emp.age
# return emp.salary   #if we define lambda function no need to create another function here because lambda is anonymous function


#s_employees = sorted(employees, key=e_sort)
#s_employees = sorted(employees, key=e_sort, reverse=True)
# s_employees=sorted(employees,key=lambda e:e.name)
s_employees = sorted(employees, key=attrgetter("name"))
s_employees = sorted(employees, key=attrgetter("age"))
# s_employees = sorted(employees) #it throws error because it does not know how to sort the employee
print(s_employees)

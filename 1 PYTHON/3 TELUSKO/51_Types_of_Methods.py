# Methods are of Threee types
# 1)Instance Methods
# i)Accessor Methods    ii)Mutator Methods
# If u want to fetch the value from instance variable use Accessor Methods
# If u want to modify value from instance variable use Mutator Methods
# 2)Class Methods
# 3)Static Methods
#
# for variables   class variables and static variables are same
# but for methods class methods and static methods are not same.they are different.

class Student:

    school="telusko"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def get_m1(self):
        return self.m1

    def set_m1(self,value):
        self.m1=value

    def avg(self):
        return(self.m1+self.m2+self.m3)/3

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is Student class in abc module")
s1=Student(36,56,63)
s2=Student(36,23,45)

print(s1.avg())
print(s2.avg())
print(Student.getSchool())
Student.info()
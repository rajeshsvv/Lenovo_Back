class student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand="HP"
            self.cpu='i5'
            self.ram=8

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1=student("Navin",40)
s2=student("Sankar",30)

# print(s1.name,s1.rollno)
# print(s2.name,s2.rollno)

s1.show()
# print(s1.lap.brand)
#
# lap1=s1.lap
# lap2=s2.lap
#
# print(id(lap1))
# print(id(lap2))
#
# lap1=student.Laptop()
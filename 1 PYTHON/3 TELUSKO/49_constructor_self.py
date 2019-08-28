class computer():
    def __init__(self):
        self.name="Ankita"
        self.age=26

    def update(self):
            self.age=28

    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False

c1=computer()
c2=computer()

# print(id(c1))
# print(id(c2))

c1.name="Azeeb"
c1.age =28

c1.update()
print(c1.name)
print(c1.age)
print(c2.name)

if c1.compare(c2):
    print("same objects")
else:
    print("They are different")
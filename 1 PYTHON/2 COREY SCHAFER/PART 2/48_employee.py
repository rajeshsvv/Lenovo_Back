class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        slef.pay = pay

    @property
    def email(self):
        return("{}.{}@gmail.com").format(self.first, self.last)

    @property
    def fullname(self):
        return("{} {}".format(self.first, self.last))

    def __repr__(self):
        return("employee('{}','{}','{}')".format(self.first, self.last, self.pay))

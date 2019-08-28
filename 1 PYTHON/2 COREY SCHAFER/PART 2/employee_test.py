import requests              # for request data from website got it


class Employee:

    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return("{}.{}@email.com").format(self.first, self.last)

    @property
    def fullname(self):
        return("{} {}".format(self.first, self.last))

    # def __repr__(self):
    #     return("employee('{}','{}','{}')".format(self.first, self.last, self.pay))

    # for mocking purpose if website is slow in the particular case got it

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def monthly_schedule(self, month):
        response = requests.get(f"http://company.com/{self.last}/{month}")
        if response.ok:
            return response.text
        else:
            return "Bad Response!"

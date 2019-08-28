# class User:
#     pass


# user1 = User()

# user1.firstname = "Sailesh"
# user1.lastname = "Jitendra"
# print(user1.firstname)
# print(user1.lastname)

# first_name = "Sahila"
# last_name = "Sudheer"

# print(first_name, last_name)

import datetime


class User:
    def __init__(self, fullname, birthday):
        self.name = fullname
        self.birthday = birthday


# extract first name and last anme from full name
        name_pieces = fullname.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        today = datetime.date(2019, 2, 13)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)


user = User("David Gutta", "19960531")

print(user.name)
print(user.first_name)
print(user.last_name)
print(user.birthday)


print(user.age())

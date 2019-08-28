import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

# Pattern matching for first mail

# pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')
# matches = pattern.finditer(emails)

# for match in matches:
#     print(match)

# Pattern matching for second mail

# pattern = re.compile(r'[a-zA-Z\.]+@[a-zA-Z]+\.(com|edu)')			# we are using group character because of match to edu or com
# matches = pattern.finditer(emails)

# for match in matches:
#     print(match)

# Pattern matching for third mail


# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')			# we are using group character because of match to edu or com
# matches = pattern.finditer(emails)

# for match in matches:
#     print(match)


# pattern matching for email generic real world example
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')			# we are using group character because of match to edu or com
matches = pattern.finditer(emails)

for match in matches:
    print(match)

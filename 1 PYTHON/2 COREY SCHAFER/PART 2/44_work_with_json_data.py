# JSON Data in Python
"""
common data format for storing some information.it is used a lot when fetching data from online apis but it is also used for 
configuration files  and different kinds of data that can be saved on your local machine 
every languages has libraries for parsing and generating JSON data

use json.loads for load JSON string into Python object

use json.dumps for load Python object into JSON string
"""


import json

people_string = """
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-444-7146",
            "emails":[ "johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "John Doe",
            "phone": "560-444-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
"""

# data = json.loads(people_string)
# # print(data)
# print(type(data["people"]))
# for person in data["people"]:
#     # print(person)
#     print(person["name"])

# now i do for convert for load JSON string into Python object so for that i use json.loads() method


data = json.loads(people_string)
# print(data)
print(type(data["people"]))

for person in data["people"]:
    # print(person)
    # print(person["name"])
    del person["phone"]

# to format the string in nice level we use indent levels then it formats nicely in output in readble format
# to format the string in nice level we use sort_keys levels then it formats in alphabetical order got it
# now i do for convert python object into JSON string so for that i use json.dump() method
new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)

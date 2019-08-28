import csv

# context manager to open a file

# html_output = ""
# names = []

# with open("29_patreons.csv", "r") as data_file:
#     csv_data = csv.reader(data_file)

#     # we dont want headers and first line of bad data
#     next(csv_data)
#     next(csv_data)

#     # print(list(csv_data))   #this statement does not prints not much readable result
#     for line in csv_data:
#         if line[0] == "No Reward":
#             break
#         names.append(f"{line[0]} {line[1]}")  # f string introduced in 3.6 to format the string
#         #names.append("{} {}".format(line[0],line[1]))

# # this code is for print all the names k
# # for name in names:
# #     print(name)
# html_output += f"<p>There are currently {len(names)} public contributers.Thank you!</p>"

# # created an HTML unorder list for 30  memebers list
# html_output += "\n<ul>"
# for name in names:
#     html_output += f"\n\t<li>{name}</li>"
# html_output += "\n</ul>"
# print(html_output)


# ANOTHER WAY to print HTML unordered list by DictReador


html_output = ""
names = []

with open("29_patreons.csv", "r") as data_file:
    csv_data = csv.DictReader(data_file)

    # we dont want first line of bad data
    next(csv_data)

    # # print(list(csv_data))   #this statement does not prints not much readable result
    for line in csv_data:
        if line["FirstName"] == "No Reward":
            break
        # names.append(f"{line["FirstName"]} {line["LastName"]}")  # f string introduced in 3.6 to format the string
        names.append("{} {}".format(line["FirstName"], line["LastName"]))

# this code is for print all the names k
# for name in names:
#     print(name)
html_output += f"<p>There are currently {len(names)} public contributers.Thank you!</p>"

# created an HTML unorder list for 30  memebers list
html_output += "\n<ul>"
for name in names:
    html_output += f"\n\t<li>{name}</li>"
html_output += "\n</ul>"
print(html_output)

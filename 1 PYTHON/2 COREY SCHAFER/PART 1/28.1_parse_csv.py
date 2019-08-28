import csv

# with open("28_names.csv", "r") as csv_file:
#     print(new_file.read())		# to read the names.csv file
#     csv_reader = csv.reader(csv_file)
#     print(csv_reader)
#     next(csv_reader)    # for eliminate the heading in result for example 1 in the sense last name not able to print on result k got it

#     # create a new file and paste the same conent in the new file as in the 28_names.csv
#     with open("28.2_copy.csv", "w") as copy_file:
#         csv_writer = csv.writer(copy_file, delimiter="\t")  		# \t in the sense tab by tab we devide the sentence like delimiter ok
#         for line in csv_reader:
#             # print(line)
#             # print(line[0])  # 0 first name 1 last name 2 email
#             csv_writer.writerow(line)


# instead of working with read and write we work on csv data with dictionary reador and dictionary writer ok corey prefer methods best methods.
# now dictionary Read
# with open("28_names.csv", "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for line in csv_reader:
#         print(line['first_name'])
#         print(line['last_name'])
#         print(line["email"])


# now dictionary write
# with open("28_names.csv", "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     with open("28.2_copy.csv", "w") as copy_file:
#         fieldnames = ["first_name", "last_name", "email"]

#         csv_writer = csv.DictWriter(copy_file, fieldnames=fieldnames, delimiter="\t")  		# \t in the sense tab by tab we devide the sentence like delimiter ok
#         csv_writer.writeheader()
#         for line in csv_reader:
#             csv_writer.writerow(line)

# to get only first name and last name without email in the 28.2 copy file taht is eeasy with dictionary read and write methods got it
with open("28_names.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open("28.2_copy.csv", "w") as copy_file:
        fieldnames = ["first_name", "last_name"]

        csv_writer = csv.DictWriter(copy_file, fieldnames=fieldnames, delimiter="\t")  		# \t in the sense tab by tab we devide the sentence like delimiter ok
        csv_writer.writeheader()
        for line in csv_reader:
            del line["email"]
            csv_writer.writerow(line)

import csv

# path = "C:\\Users\\raji\\Pictures\\Screenshots.csv_data.csv"
path = "C:\Users\raji\Pictures\Screenshots.csv_data.csv"

file = open(path, newline="")
reader = csv.reader(file)

header = next(reader)
data = [row for row in reader]


print(header)
print(data[0])



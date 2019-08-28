# fh=open("custom_file.txt")
# print(fh.read())
# print(fh.read(4))           # it will read the first four characters.
# print(fh.read(10))
# print(fh.readline())
# print(fh.readlines())           # it will read all the lines in the current file.
# print(fh.readlines()[3])
# for line in fh:
#     # print(len(line))
#     print(line.split(" "))
#     print(len(line.split(" ")))


        #   or write the above function in this way using context manager in this case no need to close the file manually.

with open("custom_file.txt") as f:
    for line in f:
        print(f.read())



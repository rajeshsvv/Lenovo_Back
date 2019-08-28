import os
newfile=open("Edureka.txt","w+")

# newfile.close()                   # when uncomment this in write mode u got i/o operation on closed file errror.

# write mode
# for i in range(1,10):
#     newfile.write("\n Welcome to Python")

# Read Mode

newfile=open("Edurekha.txt","r")
for i in range(1,10):
    # print(newfile.read())
    print(newfile.read(300))

print(newfile.mode)
print(newfile.name)
print(newfile)
# print(newfile.softspace)

newfile.seek(100)
print(newfile.read())
print(newfile.tell())
# rename the file
# os.rename("Edureka.txt","Edurekha.txt")


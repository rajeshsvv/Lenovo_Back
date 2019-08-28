fp=open("Python.txt","w+")
fp.write("So easy to learn Python\n")
fp.write("I love Python")
fp.seek(0) #seek means cursor position and starts the reading content
print(fp.read())
fp.close()
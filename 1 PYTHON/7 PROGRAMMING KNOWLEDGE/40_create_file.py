fh=open("custom_file.txt",'w')
# fh.write("The custom file creation")
try:
    for i in range(10):
        fh.write("The Line number is %d\n"%(i+1))
finally:
    fh.close()


with open("custom_file1.txt",'w') as f:
    # f.write("The Custom File is created")
    for i in range(10):
        f.write("this is line number %d\n" %(i+1))

import os
os.chdir("G:\\4 PYTHON\\PRACTICE\\BACKEND\\1 PYTHON\\9 PYTHON PROGRAMS\\PYTHON PROGRAMS LENOVO\\1_first_notes(18 Programs)")
with open("count_letters.txt",'r') as f:
    count=0
    for i in f.read():
        if i.isupper():
            count+=1
    print(count)


os.chdir("PYTHON PROGRAMS LENOVO/1_first_notes(18 Programs)/count_letters.txt")
with open("G:\\4 PYTHON\\PRACTICE\\BACKEND\\1 PYTHON\\9 PYTHON PROGRAMS\\PYTHON PROGRAMS LENOVO\\1_first_notes(18 Programs)\\count_letters.txt") as f:
    count=0
    text=f.read()
    for i in text:
        if i.isupper():
            print(i)
        count+=1



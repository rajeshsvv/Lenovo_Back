import os  # navigate the file system and change the file names etc
os.chdir("H:/VIDEOS/ENTERTAINMENT/TELUGU/Comedy Scenes")
print(os.getcwd())
for f in os.listdir():
    # print(f)
    # print(os.path.splitext(f))   	# to split the text in file name  so we write os.path remember it
    # file_name, file_extension = os.path.splitext(f)
    # print(file_name.split("-"))

    f_name, f_extension = os.path.splitext(f)
    f_title, f_comedy, f_num = f_name.split("-")
    # print(f_num)
    f_num = f_num.strip()[1:].zfill(2)									# for remove the # character before number
    # print("{}-{}-{}{}".format(f_num, f_comedy, f_title, f_extension))
    # print("{}-{}{}".format(f_num, f_title, f_extension))
    new_name = "{}-{}{}".format(f_num, f_title, f_extension)
    os.rename(f, new_name)
    # if there is any space after title in result f_title=f_title.strip() use this okay

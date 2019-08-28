# OS Module allows us to interact with unnderlying operating systems in several diffrent ways
# so for example we can navigate to file system and get file information look up and change the environment variables
# we can move files arround and all kinds of useful steps.
import os

# print(dir(os))  						# we can accesss attributes and Methods in the OS module
# # os.mkdir("HI-2/Sub-Dir-1")
# os.makedirs("HI-2/Sub-Dir-1")			#use this for creating tree type directories ok

# for remove the directories

# os.rmdir("HI-2/Sub-Dir-1")				#rmdir does not remove the intermediate directoires ok
# os.removedirs("HI-2/Sub-Dir-1")  			# removedir removes intermediate directories also use this directory k  					# getcwd means get current directory
# os.chdir("F:\4 PYTHON\PRACTICE")		# chdir means change directory
# print(os.listdir())  					# listdir it gives the list of files and folders in the curent directory


# os.mkdir("HI-2/Sub-Dir-1")
# os.makedirs("HI-2/Sub-Dir-1")			#use this for creating tree type directories ok

# for remove the directories

# os.rmdir("HI-2/Sub-Dir-1")				#rmdir does not remove the intermediate directoires ok
# os.removedirs("HI-2/Sub-Dir-1")  			# removedir removes intermediate directories also use this directory k

# we want to rename file or folder
#os.rename("text.txt", "demo.txt")

"""
from datetime import datetime
print(os.stat("demo.txt"))      			# stat to know the details in the text file
print(os.stat("demo.txt").st_size)
print(os.stat("demo.txt").st_mtime)
mod_time = os.stat("demo.txt").st_mtime
print(datetime.fromtimestamp(mod_time))
"""


# walk we want to see the entire directory tree and files with in the certain location
# if u want to traverse the directory tree and print all of the directories in the file
# for dirpath, dirnames, filenames in os.walk("F:/4 PYTHON/PRACTICE/2 COREY SCHAFER")
# print("Current Path", dirpath)
# print("Directories", dirnames)
# pirnt("Files", filenames)
# os.walk()

# print(os.environ)
# print(os.environ.get("HOME"))
# print(os.path.basename("/temp/test.txt"))
# print(os.path.dirname("/temp/test.txt"))
# print(os.path.split("/temp/test.txt"))
# print(os.path.exists("/temp/test.txt"))
print(os.path.splitext("/temp/test.txt"))
print(os.path)
# # os.mkdir("HI-2/Sub-Dir-1")
# os.makedirs("HI-2/Sub-Dir-1")			#use this for creating tree type directories ok

# for remove the directories

# os.rmdir("HI-2/Sub-Dir-1")				#rmdir does not remove the intermediate directoires ok
# os.removedirs("HI-2/Sub-Dir-1")  			# removedir removes intermediate directories also use this directory k

import random

feet_in_module=5280
meters_in_kilometer=1000
beatles=["C","C++","Java","Dotnet","Perl","Python"]

def get_file_extn(filename):
    return filename[filename.index(".")+1:]

def roll_dice(num):
    return random.randint(1,num)

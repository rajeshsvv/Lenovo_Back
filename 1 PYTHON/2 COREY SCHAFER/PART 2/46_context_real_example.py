import os
from contextlib import contextmanager

# cwd = os.getcwd()
# os.chdir("Sample-Dir-One")
# print(os.lisdir())
# os.chdir(cwd)

# cwd = os.getcwd()

# os.chdir("Sample_Dir_Two")
# print(os.istdir())
# os.chdir(cwd)

# we can simplify the code like the below k for above code


@contextmanager
def change_dir(destination):
    try:
        cmd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir("sample-dir_one"):
    print(os.listdir())

with change_dir("sample_dir_two"):
    print(os.listdir())

# context managers
"""
couple of different ways we can write context managers
1)we can either do this by class
2)we can use function with decorator
"""

# first write through class


"""

class Open_File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


with Open_File("46_context_class.txt", "w") as f:
    f.write("Start Writing Corey")

print(f.closed)

"""


# using context lib second through function

"""

from contextlib import contextmanager


@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()

# f = open(file, mode)
# yield f
# f.close()


with open_file("46_context_generator.txt", "w") as f:
    f.write("Corey Please Help me to complete this task")

print(f.closed)

"""
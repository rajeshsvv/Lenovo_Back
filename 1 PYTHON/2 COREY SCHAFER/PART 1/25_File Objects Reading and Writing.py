# File Object How to read and write File in Python using COntext manager
# Reading(r) Writing(w) Appending(a) or Reading and Writing(r+) Operations on File Default is Reading if we dont mention anything

# context manager use is no need to mention the close the file it automatically take care about that.
# with open("text File.txt", "r") as f:
#     pass

# print(f.closed)


with open("text File.txt", "r") as f:
    f_content = f.read()
    f_content = f.read(100)
    print(f_content, end="")
# f_content = f.read(100)
# print(f_content, end="")
# f_content = f.readlines()
# f_content = f.readline()
# print(f_content, end="")
# f_content = f.readline()
# print(f_content, end="")

# for line in f:
#     print(line, end="")

# print(f.closed)   #no need to mention this line when we are in context manager it will take care of that
# print(f.read())	#IO operation on closed file error it gets

# size_to_read = 10

# f_contents = f.read(size_to_read)
# print(f_contents, end="")
# f.seek(0)
# f_contents = f.read(size_to_read)
# print(f_contents)
# print(f.tell())
# while len(f_contents) > 0:
#     print(f_contents, end="*")
#     f_contents = f.read(size_to_read)

# f.write("test")
# with open("text2.txt", "w") as f:
#         # pass  # pass in the sense dont do anything rightnow with this function use it later otherwise no error k
#     f.write("Test")
#     f.seek(0)
#     f.write("R")

# read and write operations
# with open("text File.txt", "r") as rf:
#     with open("text_copy.txt", "w") as wf:
#         for line in rf:
#             wf.write(line)


# for pics purpose we use rb and wb because pics are in string mode its not work actually
# we havee to convert in binary mode so for that we use rb and wb

# with open("Nazria.jpg", "rb") as rf:
#     with open("Nazria_1.jpg", "wb") as wf:
#         # for line in rf:
#         #     wf.write(line)

#         chunk_size = 4096
#         rf_chunk = rf.read(chunk_size)
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk = rf.read(chunk_size)

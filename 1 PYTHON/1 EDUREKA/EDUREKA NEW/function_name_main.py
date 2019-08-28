def func():
    print("func in one.py")

print("top level in one.py")

if __name__=="__main__":
    print("one.py is directly running")
else:
    print("one.py is import to another module")

import function_name_main

def func():
    print("func in one.py")

print("top level in two.py")
function_name_main.func()

if __name__=="__main__":
    print("two.py is directly running")
else:
    print("two.py is import to another module")
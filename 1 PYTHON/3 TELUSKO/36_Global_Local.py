#      VARIABLE SCOPE            LOCAL       GLOBAL      ENCLOSED    BUILT IN

a=15                        #global variable->outside the function->access anywhere in the file
print(id(a))
def something():
    # global a              #use this if u want to change the global variable value
    x=globals()['a']
    print(id(x))
    a=20                  #local variable->in side the function->access inside the function only
    globals()['a']=30

    print("inside the function",a)

something()

print("outside the function",a)
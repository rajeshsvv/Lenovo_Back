'''
#Nested Function:

def outer_function(text):
    def inner_function():
        print(text)
    inner_function()
    # outer_function(text)        # maximum recursion depth exceeded

outer_function(text="Rajesh")
'''

'''
def pop(list):
    def get_last_iem(my_list):
        return my_list[len(list)-1]
    list.remove(get_last_iem(list))
    return list

a=[1,2,3,4,5,6]

print(pop(a))
print(pop(a))
print(pop(a))
print(pop(a))
print(pop(a))
print(pop(a))
print(pop(a))

# for i in a:
#     print(a)
'''

# CLOSURE FUNCTION
'''
def outer_function(test):
    def inner_function():
        print(test)
    return inner_function


a=outer_function("HI")          # now a contains the innner_function value

# del outer_function
# outer_function("Hello")       # now result is outer function is not defined because u already deleted.

del outer_function              # it will store the some kind of result into the memory.
(a())
'''

# Another Closure Example       8:09:57

def nth_pow(exponent):
    def pow_of(base):
        return (pow(base,exponent))
    return pow_of

square=nth_pow(5)
print(square(2))
print(square(3))
print(square(4))
print("---")
qube=nth_pow(3)         # now we find cube for the numbers
print(qube(3))
print(qube(4))
print(qube(5))



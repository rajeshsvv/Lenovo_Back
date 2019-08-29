'''
a = [1,2,2,3]
print(list(set(a)))


print(sum(range(1,10)))
'''

globvar = 0
def set_globvar_to_one():
    global globvar    # Needed to modify global copy of globvar
    globvar = 1
def print_globvar():
    print(globvar)     # No need for global declaration to read value of globvar
set_globvar_to_one()
print(print_globvar())



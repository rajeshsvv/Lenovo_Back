# Arguments have two types
# 1)Actual Arguments  (positional,keyword,default,variable length)
# 2)Formal Arguments  ()

# def add(a,b):           #Formal Arguments
#     c=a+b
#     print(c)
#
# add(2,3)                #Actual Arguments

# def person(name,age=18):
#     print(name)
#     print(age-4)

# person("Naveen",35)                   #positional arguments
# person(age=35,name="Naveen")        #keyword Arguments
# person("Naveen")                      #default Arguments


# variable length arguments

#we can define a define a function and we dont know how many arguments are there k (variable length arguments)

#this is basic function just for reference for adding the two numbers
# def sum(a,b):
#     c=a+b
#     print(c)
#
# sum(5,6)

def sum(a,*b):
    #c=a+b

    c=a

    for i in b:
        c=c+i

    print(c)

sum(5,6,7.5,8)
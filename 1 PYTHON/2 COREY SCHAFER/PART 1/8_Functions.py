# Functions are set of instructions packaged togther to perform some tasks
# benifit of functions are reusable of code without repeat ourself

'''
def hello_funct():
	pass
print(hello_funct)
print(hello_funct())
'''

'''
def hello_funct():
	print("Hello Function.")

hello_funct()
hello_funct()
hello_funct()
'''

'''
def hello_funct():
	return "Hello Function."

print(hello_funct().upper())
print(hello_funct().lower())
print(hello_funct())append()
'''

'''
def hello_funct(greeting):
    return "{} Function.".format(greeting)


print(hello_funct("Corey"))
'''

# name ="you" in the sense setting default value means when we dont pass name parameter to te function it prints Corey You ok
'''
def hello_funct(greeting,name="You"):
	return "{},{}.".format(greeting,name)

print(hello_funct("Corey"))
print(len("Test"))
'''

'''
def hello_funct(greeting,name):
	return "{},{}.".format(greeting,name)

print(hello_funct("Corey",name="Rajesh"))
'''

# args is postional arguments where kwargs is keyword arguments
'''
def student_info(*args,**kwargs):
	print(args)
	print(kwargs)

student_info("Science","Social",name="Corey",age=30)
'''


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ['Science', 'Social']
info = {'name': 'Corey', 'age': 30}

student_info(courses, info)
student_info(*courses, **info)


print(len("Test"))

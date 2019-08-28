
import random
'''
num=random.randrange(10)               #   generate random integer within the given range everytime u run it u get different number
print(num)

ran=random.randrange(0,100,15)           #   return a randomly select element  from range(start,stop,step) with multiples of 15 k
print(ran)

inter=random.randint(0,30)              #   return random integer N such that a<=N<=b
print(inter)
'''

#print(random.getstate())                 # returns an object capturing the current internal state of the generator.

print(random.uniform(6,20))               #  returns a random floating point number  N such that a<=N<=b for a<=b
                                                                                                #a>=N>=b for a>b

print(random.randint(5,7))
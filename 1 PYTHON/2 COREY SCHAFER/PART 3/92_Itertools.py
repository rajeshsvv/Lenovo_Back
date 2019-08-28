# itertools is collection of tools that allows us to work with iterators in a fast and memory efficient way.

# iterator is sequential data that we can iterate or loop over hold one eobject in  memory at a time.
# zip function combines two iterables and pairs the values together.


# list of itertool methods
# 1-counter,2-cycle,3-repeat


# 1-count

'''
import itertools
# count=itertools.count()
count=itertools.count(start=5,step=5)
count=itertools.count(start=5,step=-2.5)
print(count)

# for i in counnt:
#     print(i)

print(next(count))
print(next(count))
print(next(count))
print(next(count))



daily_data=[1000,200,"Sanju","Bhargavi"]

# result=zip(itertools.count(),list)              # one result at a time
# print(next(result))

result=list(zip(itertools.count(),daily_data))
result=list(zip(range(10),daily_data))
result=list(itertools.zip_longest(range(10),daily_data))
print(result)

'''

# 2-cycle  it also return iterator hat goes on forever
'''
import itertools
count=itertools.cycle([2,3,4])
count=itertools.cycle(("On","Off"))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
'''

# 3-repeat it just takes input and repeats it indefinitely.

'''
import itertools

count=itertools.repeat(2)
count=itertools.repeat(2,times=3)
count=map(pow,range(10),itertools.repeat(9))
print(list(count))

for i in count:
    print(i)

# print(next(count))
# print(next(count))
# print(next(count))
# print(next(count))
'''

#4-starmap

'''
import itertools

squares=itertools.starmap(pow,[(0,2),(2,4),(4,6)])
print(list(squares))

'''

#5-Permutations and combinaions
# combinationas are that we can group a certain number of items or order does not matter
# permutations are all different ways that u can group certain number of items where order does matter
# permutations and combinations dont repeat values.

'''
import itertools

a=['a','b','c','d','e']

result=itertools.combinations(a,2)
# result=itertools.permutations(a,2)

# print(next(result))
# print(next(result))

for i in result:
    print(i)
'''

#6-prodcut function

'''
import itertools

numbers=[1,2,3,4,5]
result=itertools.product(numbers,repeat=2)
result=itertools.combinations_with_replacement(numbers,3)

for item in result:
    print(item)
    
'''

# 7-chain function

# it will allow us to chain together iterables so that it will go through all the items in the first iterable and after
# that it has been exhausted

'''
import itertools

letters=['a','b','c','d','e']
numbers=[1,2,3,4,5,6]
names=["Corey","Nickle"]

combined=itertools.chain(letters,numbers,names)
for item in combined:
    print(item)
'''

#   8-slice function performs slicing on ana iterator and this function is called islice.


'''
# import itertools
# 
# letters=['a','b','c','d','e']
# numbers=[0,1,2,3,2,1,0]
# names=["Corey","Nickle"]

# combined=itertools.islice(range(10),8)
# combined=itertools.islice(range(10),1,5,2)
# for item in combined:
#     print(item)


with open('92_text.log','r') as f:
    # content=f.read()
    content=itertools.islice(f,4)

    for line in content:
        print(line,end="")
'''


'''
functions for select certain elements from an iterable first
filter is for determine whether something True or false.
compress is for those values are just passed in as ierable.
dropwhile function
will drop values from an iterable until one of the values return true
takewhile function 

'''

# compress function

# letters=['a','b','c','d']
# selecters=[True,True,True]
#
# result=itertools.compress(letters,selecters)
# for item in result:
#     print(item)



'''
def lt_2(n):
    if n<2:
        return True
    return False

# result=filter(lt_2,numbers)
# result=itertools.filterfalse(lt_2,numbers)
result=itertools.dropwhile(lt_2,numbers)
result=itertools.takewhile(lt_2,numbers)

for item in result:
    print(item)
# print(result)
'''


#accumulate functon

# this takes an iterable and returns accumulated sums of each item

'''

import itertools
import operator

letters=['a','b','c','d','e']
numbers=[0,1,2,3,2,1,0]
names=["Corey","Nickle"]

numbers=[1,2,3,4,5,6,7,8]
result=itertools.accumulate(numbers)
result=itertools.accumulate(numbers,operator.__mul__)

for i in result:
    print(i)

'''


                                    # important             groupby function

# this will go through an iterable and group values based on a certain key and then it will return a stream of tuples.


import itertools


people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

def get_state(person):
    return person['state']

person_group=itertools.groupby(people,get_state)

copy1,copy2=itertools.tee(person_group)
print(copy1,copy2)
for key,val in person_group:
    print(key,len(list(val)))
    # print(key)
    # for person in val:
    #     print(person)
    # print()

    # replicate the iterator using T function.


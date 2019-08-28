
# how to create a empty set

# s1={}             # this will create empty dictionary
# s1=set()
# print(s1)

# how create a set

"""
s1=set([1,2,3,4,5,5,4,3,2,1])
print(s1)

# or

# s={1,2,3,4,5}
# print(s)

# add single value
s1.add(6)
print(s1)

# add multiple values
s1.update([6,7,8,9])
print(s1)
s2=set([7,8,9])
s1.update([6,7,8,100],s2)
print(s1)

# delete elements which are exist
s1.remove(100)
s1.discard(9)
print(s1)

# delete elements which are not exist
s1.remove(101)        #error
s1.discard(8)        #nothing
print(s1)

"""

# Operations on sets like union intersection

'''
s1={1,2,3}
s2={2,3,4}
s3={3,4,5}


s4=s1.intersection(s2)
print(s4)
s4=s1.intersection(s2,s3)
print(s4)

s4=s1.difference(s2)
print(s4)

# want values in s2 but not in s1 and s3
s4=s2.difference(s1,s3)         #{1}
print(s4)
s4=s3.difference(s1,s2)
print(s4)

s4=s1.difference(s2)
print(s4)

s4=s1.symmetric_difference(s2)      #{1,4}
print(s4)

'''

# l1=[1,2,3,4,4,3,2,1]
# print(list(set(l1)))        #remove duplicates result {1,2,3,4}

employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']

gym_members = ['April', 'John', 'Corey']

developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

result=set(gym_members).intersection(developers)
print(result)
result=set(employees).difference(gym_members,developers)
print(result)

if "Corey" in developers:
    print("Found!")

# O(n) for list     # scan the whole list until it finds the value
# O(l) for set      #its just constant time


x = None
print(x)

# NUMERIC
num = 4
print(type(num))

num = 4.6
print(type(num))
# represent complex number with j instead of i in python k got it
num = 4 + 6j
print(type(num))


a = 5.6
b = int(a)
print(b)
print(type(b))
c = complex(b, a)
print(c)
print(b < a)


print(int(True))
print(int(False))


list = [10, 20, 30, 40, 50]
print(list)
print(type(list))

set = {10, 90, 80, 60, 70, 23.87, 70}
print(set)
print(type(set))


tuple = (52, 45, 12, 36, 85, 79, 41, 96)
print(tuple)
print(type(tuple))

dictionary = {1: 23, 2: 56, 3: 89, 5: 23}
print(dictionary)
print(type(dictionary))
print(dictionary[3])
print(dictionary.get(1))

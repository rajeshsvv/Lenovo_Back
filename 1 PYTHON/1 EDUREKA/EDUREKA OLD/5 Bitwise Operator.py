num1=6  #110
num2=2  #010

#AND     001-2
#OR      110-6
#xor=    100-4

print("Bitwise and=",num1 & num2)
print("Bitwise OR=",num1 | num2)
print("Bitwise XOR=",num1 ^ num2)

#Right Shift and Left Shift

print("Num1 right shift by 2 positions",num1>>2)
print("Num2 Left shift by 2 positions",num2<<2)
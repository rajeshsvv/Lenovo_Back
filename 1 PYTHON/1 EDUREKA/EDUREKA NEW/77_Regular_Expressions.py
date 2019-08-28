import re

'''
print(re.sub(r'[a]','*','abcde abcedf abcdef'))
print(re.sub(r'[abc]','@','abcdef abcdef'))                   # it replaces the * with where it contains abc
                                                              # abc in this case it will search for abc sequence
                                                              #[abc] in this case it will search for a,b,c individual chars
print(re.sub(r'[abc]','*','Hello How are you man'))
print(re.sub(r'abc','*','Hello How are you man'))
print(re.sub("AB+","*",'AB ABBBBBBBBB ABCCCC ADDDDD'))

print(re.sub(r'^abc','*','abcdef abcdef'))
print(re.sub(r'abc$',"#",'abcdefg ijkalmabc'))
print(re.sub(r'abc','@',"abcdef ijklmnabc"))
'''


print(re.search(r'ab','Here is an absolute string'))        # search looks for pattern anywhere in the string
print(re.match(r'ab',"Here is an absolute string"))         # match looks for string at the beginning of the string only.
print(re.match(r'ab',"abhi Here is an absolute string"))


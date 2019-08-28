# Conditional Statements
# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

language = "DJango"

if language == "Python":
    print("Language is Python")
elif language == 'Java':
    print("Language is Java")
elif language == "Javascript":
    print("Language is Javascript")
else:
    print("No Language")

# False Values:
"""
False
None
Zero of any numeric type means if u put 0 at condition it will become False got it
Any Empty Sequence.For Example (),[],'',
Any Empty Mapping.For Example {}
"""

# condition=False
# condition=None
# condition=0
condition = 10
# condition=''

if condition:
    print("Evaluated to True")
else:
    print('Evaluated to False')

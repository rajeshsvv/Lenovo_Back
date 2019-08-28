is_male=False
is_tall=False

if is_male and is_tall:
    print("You are  tall male")
elif is_male and not(is_tall):
    print("You are male person but short one candidate")
elif not(is_male) and is_tall:
    print("You are not male but tall one person")
else:
    print("You are  not a male and not a tall")
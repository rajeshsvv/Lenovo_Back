def lbs_to_kg(weight):
    return weight*.5

def kg_to_lbs(weight):
    return weight/.45

def find_max(numbers):
    maximum=numbers[1]
    for number in  numbers:
        if number>maximum:
            maximum=number
    return maximum

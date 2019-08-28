# Generate Random Numbers
# should not be used for cryptography and security purposes these Random Module	use Secret Module instead of the random Module
# Random Module is for generate Random Data or game or need some Random Values or shuffle some values  perfect for random modules
# list of methods-> random-uniform-choice-choices-shuffle-sample

import random  # this is standard library no need to install from third party library


# value = random.random()
# value = random.uniform(1, 10)  # random floating point value in between 1 and 10
# value = random.randint(1, 6)  # random int point value in between 1 and 5
# print(value)

# Example for choice to get random value from list of valuees
# greeting = ["Hello", "Hi", "Hey", "Howdy", "Hola"]
# random_greet = random.choice(greeting)
# print(random_greet + ":Option Selected")

# example for choices to get random values from list of values
#colors = ["red", "blue", "green", "purple"]
# random_colors = random.choices(colors, k=10)  # herre k in the sense how many times it give random values
# random_colors = random.choices(colors, weights=[18, 18, 18, 2], k=10)
# print(random_colors)


# randomly shuffle list of values
# deck = list(range(1, 53))
# random.shuffle(deck)					# to shuffle the 52 cards randomly use shuffle ok
# print(deck)


# to get 5 unique cards every time from 52 cardds
deck = range(1, 53)
random_deck = random.sample(deck, k=5)
print(random_deck)

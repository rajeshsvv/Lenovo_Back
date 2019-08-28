
# impliment generator when u impliment genrator no need to impliment next dunder method k
def sentense(sentence):
    for word in sentence.split():
        yield word

my_sentense=sentense("Corey is excellent")

for word in my_sentense:
    print(word)


# print(next(my_sentense))
# print(next(my_sentense))
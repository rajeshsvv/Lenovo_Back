# through class impliment iterator

class iterat:
    def __init__(self,sentense):
        self.sentense=sentense
        self.index=0
        self.words=self.sentense.split(" ")

    def __iter__(self):
        return self.sentense

    def __next__(self):
        if self.index>=len(self.words):
            raise StopIteration
        index=self.index
        self.index+=1
        return self.words[index]

s=iterat("Hi Rajesh")
print(s.__next__())
print(s.__next__())
print(s.__iter__())


# thorugh genrator

def sentense(words):
    for word in words.split(","):
        yield word

result=sentense("This is text")
for word in result:
    print(word)
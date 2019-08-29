class Accesser:
    def __init__(self):
        self.foo=11
        self._bar=121
        self.__private=15

a=Accesser()
print(dir(a))           # in output window able to see foo bar but for __private with class name we are able to see

a.foo=25
a._bar=63
Accesser.__private=85
print(a.foo)
print(a._bar)
print(Accesser.__private)


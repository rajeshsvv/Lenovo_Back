# two aspects of Pythonic
# Duck Typing and easier to ask forgiveness than permission(EAFP)


class Duck:
    def quack(self):
        print("Quack,Quack")

    def fly(self):
        print("Flap,Flap")


class Person:
    def quack(self):
        print("Iam quaking like duck")

    def fly(self):
        print("Iam flaping like Arms")


# def quack_and_fly(thing):
    # not Duck Typed (Non-Pythonic)
    # if isinstance(thing, Duck):
    # thing.quack()
    # thing.fly()
    # else:
    #     print("This has to be Duck")
#      print()


# def quack_and_fly(thing):
#     # LBYL (Non-Pythonic)
#     if hasattr(thing, 'quack'):
#         if callable(thing.quack):
#             thing.quack()

#     if hasattr(thing, 'fly'):
#         if callable(thing.fly):
#             thing.fly()
    # print()

def quack_and_fly(thing):
        # EAFP(Pythonic)
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

    print()


d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

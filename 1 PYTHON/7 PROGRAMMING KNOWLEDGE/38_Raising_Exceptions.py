class CoffeeCup:
    def __init__(self,temperature):
        self.__temperature=temperature
    def DrinkCoffe(self):
        if self.__temperature>85:
            # print("Coffee is too hot")
            raise Exception("Coffee is too hot")
        elif self.__temperature<65:
            # print("Coffee is too cold")
            raise ValueError("Coffee is too cold")
        else:
            print("Coffee 0k to drink")

cup=CoffeeCup(80)
cup.DrinkCoffe()

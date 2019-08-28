class CoffeeTooHotException(Exception):
    def __init__(self,msg):
        super().__init__(msg)
class CoffeeTooColdException(Exception):
    def __init__(self,msg):
        super().__init__(msg)


class CoffeeCup:
    def __init__(self,temperature):
        self.__temperature=temperature
    def DrinkCoffe(self):
        if self.__temperature>85:
            # print("Coffee is too hot")
            raise CoffeeTooHotException("Coffee Temperature:"+str(self.__temperature))
        elif self.__temperature<65:
            # print("Coffee is too cold")
            raise CoffeeTooColdException("Coffee Temperature:"+str(self.__temperature))
        else:
            print("Coffee 0k to drink")

cup=CoffeeCup(20)

cup.DrinkCoffe()

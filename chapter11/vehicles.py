class Automobile:
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_milege(self):
        return self.__mileage
    
    def get_price(self):
        return self.__price
    
class Car(Automobile):
    def __init__(self, make, model, mileage, price, doors):
        Automobile.__init__(self, make, model, mileage, price)
        self.__doors = doors

    def set_doors(self, doors):
        self.__doors = doors

    def get_doors(self):
        return self.__doors
    
    def __str__(self):
        return (
            f"Изготовитель: {self.get_make()}\n" +
            f"Модель: {self.get_model()}\n" +
            f"Пробег: {self.get_milege()}\n" +
            f"Цена: {self.get_price()}\n" +
            f"Количество дверей: {self.get_doors()}"
        )
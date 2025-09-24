class Mammal:
    def __init__(self, species):
        self.__species = species

    def show_species(self):
        print("Я -", self.__species )

    def make_sound(self):
        print("Грррррр")

class Dog(Mammal):
    def __init__(self):
        Mammal.__init__(self, "Собака")

    def make_sound(self):
        print("Гав-гав")


class Cat(Mammal):
    def __init__(self):
        Mammal.__init__(self, "Кот")

    def make_sound(self):
        print("Мяу")
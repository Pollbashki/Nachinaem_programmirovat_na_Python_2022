from animals import Cat, Dog, Mammal

def main():
    mammal = Mammal("Обычное животное")
    cat = Cat()
    dog = Dog()

    # Показать информацию о каждом животном.
    print('Вот несколько животных и')
    print('звуки, которые они издают.')
    print('-------------------------')
    show_mammal_infо(mammal)
    print()
    show_mammal_infо(dog)
    print()
    show_mammal_infо(cat)

def show_mammal_infо(creature):
    creature.show_species()
    creature.make_sound()

if __name__ == "__main__":
    main()
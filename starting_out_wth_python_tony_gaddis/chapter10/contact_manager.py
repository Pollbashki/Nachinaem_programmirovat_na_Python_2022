from contact import Contact
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = "contacts.dat"

def main():
    mycontacts = load_contacts()

    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)

    save_contacts(mycontacts)

def load_contacts():
    try:
        inputfile = open(FILENAME, 'rb')

        contact_dct = pickle.load(inputfile)

        inputfile.close()
    except IOError:
        contact_dct = {}

    return contact_dct

def get_menu_choice():
    print()
    print('Меню')
    print ('-------------------------------------- ')
    print('1. Найти контактное лицо')
    print('2. Добавить новое контактное лицо')
    print('3. Изменить существующее контактное лицо')
    print('4. Удалить контактное лицо')
    print('5. Выйти из программы')
    print()

    choice = int(input("Введите выбранный пункт: "))

    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Введите выбранный пункт: "))

    return choice

def look_up(mycontacts):
    name = input('Введите имя: ')

    print(mycontacts.get(name, "'Это имя не найдено."))

def add(mycontacts):
    name = input('Имя: ')
    phone = input('Телефон: ')
    email = input('Электронный адрес: ')

    entry = Contact(
        name=name,
        phone=phone,
        email=email
    )

    if name not in mycontacts:
        mycontacts[name] = entry
    else:
        print('3TO имя уже существует.')

def change(mycontacts):
    name = input('Введите имя: ')

    if name in mycontacts:
        phone = input('Введите новый номер телефона: ')
        email = input('Введите новый электронный адрес: ')

        entry = Contact(
            name=name,
            phone=phone,
            email=email
        )

        mycontacts[name] = entry
        print('Информация обновлена.')

    else:
        print('Это имя не найдено.')

def delete(mycontacts):
    name = input('Введите имя: ')
    if name in mycontacts:
        del mycontacts[name]
        print('Запись удалена.')
    else:
        print('Это имя не найдено.')


def save_contacts(mycontacts):
    output_file = open(FILENAME, 'wb')

    pickle.dump(mycontacts, output_file)

    output_file.close()


if __name__ == "__main__":
    main()
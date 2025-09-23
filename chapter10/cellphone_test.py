from cellphone import CellPhone

def main():
    phones = make_list()

    print("Вот введенные Вами данные:")
    display_list(phones)


def make_list():
    phone_list = []

    print('Введите данные о пяти телефонах.')
    for count in range(1, 6):
        print('Номер телефона ' + str(count) + ':')
        man = input("Введите производителя: ")
        mod = input("Введите модель: ")
        retail = float(input("Введите розничную цену: "))
        print()

        phone = CellPhone(
            manufact=man,
            model=mod,
            price=retail
        )

        phone_list.append(phone)

    return phone_list


def display_list(phone_list):
    for item in phone_list:
        print(f"Производитель: {item.get_manufact()}")
        print(f"Модель телефона: {item.get_mmodel()}")
        print(f"Розничная цена: $ {item.get_retail_price():,.2f}")


if __name__ == "__main__":
    main()
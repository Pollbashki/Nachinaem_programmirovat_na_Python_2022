from cellphone import CellPhone

def main():
    man = input("Введите производителя: ")
    mod = input("Введите модель: ")
    retail = float(input("Введите розничную цену: "))

    phone = CellPhone(
        manufact=man,
        model=mod,
        price=retail
    )

    print(f"Производитель: {phone.get_manufact()}")
    print(f"Модель телефона: {phone.get_mmodel()}")
    print(f"Розничная цена: $ {phone.get_retail_price():,.2f}")

if __name__ == "__main__":
    main()
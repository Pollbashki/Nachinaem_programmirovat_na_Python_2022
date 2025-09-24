from vehicles import Car, Truck, SUV

def main():
    used_car = Car('Audi', 2007, 12500, 21500.0, 4)

    truck = Truck('Toyota', 2002, 40000, 12000.0, '4WD')

    suv = SUV('Volvo', 2000, 30000, 18500.0, 5)

    print('ПОДЕРЖАННЫЕ АВТО НА СКЛАДЕ')
    print('==========================')

    print(
        "Данный легковой автомобиль имеется на складе.",
        used_car,
        "Данный пикап имеется на складе.",
        truck,
        "Данный джип имеется на складе.",
        suv,
        sep='\n')

if __name__ == "__main__":
    main()
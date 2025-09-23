from coin import Coin

def main():
    my_coin = Coin()

    print("Эта сторона обращена вверх, ", my_coin.get_sideup())

    print("Подбрасываем монетку...")
    my_coin.toss()

    print("Эта сторона обращена вверх, ", my_coin.get_sideup())

if __name__ == '__main__':
    main()
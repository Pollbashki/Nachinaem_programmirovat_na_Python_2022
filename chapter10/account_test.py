from bankaccount import BankAccount

def main():
    start_balance = float(input("Введите свой начальный остаток: "))

    savings = BankAccount(balance=start_balance)

    pay = float(input('Сколько Вы получили на этой неделе? '))
    print('Вношу эту сумму на Ваш счет.')
    savings.deposit(pay)

    print(savings)

    cash = float(input("Какую сумму желаете снять со счета? "))
    print('Снимаю эту сумму с Вашего банковского счета.')
    savings.withdraw(amount=cash)

    print(savings)

if __name__ == "__main__":
    main()
from bankaccount import BankAccount

def main():
    start_balance = float(input("Введите свой начальный остаток: "))

    savings = BankAccount(balance=start_balance)

    pay = float(input('Сколько Вы получили на этой неделе? '))
    print('Вношу эту сумму на Ваш счет.')
    savings.deposit(pay)

    print(f"Ваш остаток на счете составляет $ {savings.get_balance():,.2f}.")

    cash = float(input("Какую сумму желаете снять со счета? "))
    print('Снимаю эту сумму с Вашего банковского счета.')
    savings.withdraw(amount=cash)

    print(f"Ваш остаток на счете составляет $ {savings.get_balance():,.2f}.")

if __name__ == "__main__":
    main()
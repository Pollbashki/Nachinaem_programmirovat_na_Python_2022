# Класс BankAccount имитирует банковский счет.

class BankAccount():
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Ошибка: недостаточно средств")

    def get_balance(self):
        return self._balance
    
    def __str__(self):
        return f"Остаток на счете $ {self.get_balance():,.2f}"
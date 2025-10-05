# Тестовая программа, использующая счета
# Версия 1, использующая явные переменные для каждого объекта Account

from Account import *

oJoesAccount = Account('Joe', 100, 'JoesPassword')
print("Created an account for Joe")

oMarysAccount = Account('Mary', 12345, 'MarysPassword')
print("Created an account for Mary")

oJoesAccount.show()
oMarysAccount.show()
print()

# вызываем разные методы для разных счетов
print('Calling methods of the two accounts ...')
oJoesAccount.deposit(50, 'JoesPassword')
oMarysAccount.withdraw(345, 'MarysPassword')
oMarysAccount.deposit(100, 'MarysPassword')

# отображаем счета
oJoesAccount.show()
oMarysAccount.show()
# Тестовая программа, использующая счета
# Версия 2, с использованием списка счетов

from Account import *

accountList = []

oAccount = Account('Joe', 100, 'JoesPassword')
accountList.append(oAccount)
print("Joe's account number is 0")

oAccount = Account('Mary', 12345, 'MarysPassword')
accountList.append(oAccount)
print("Mary's account number is 1")

accountList[0].show()
accountList[1].show()
print()

# вызываем разные методы для разных счетов
print('Calling methods of the two accounts ...')
accountList[0].deposit(50, 'JoesPassword')
accountList[1].withdraw(345, 'MarysPassword')
accountList[0].deposit(100, 'MarysPassword')

# отображаем счета
accountList[0].show()
accountList[1].show()

# создаем новый счет с информацией от пользователя
print()

userName = input('What is the name for the new user account? ')
userBalance = input('What is the starting balance for this account? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account? ')

oAccount = Account(name=userName, balance=userBalance, password=userPassword)
accountList.append(oAccount)

# отображаем вновь созданный счет пользователя
print('Created new account, account number is 2')
accountList[2].show()

# вносим 100 на новый счет
accountList[2].deposit(100, userPassword)
usersBalance = accountList[2].getBalance(userPassword)
print()
print("After depositing 100, the user's balance is:", usersBalance)
# отображаем новый счет
accountList[2].show()
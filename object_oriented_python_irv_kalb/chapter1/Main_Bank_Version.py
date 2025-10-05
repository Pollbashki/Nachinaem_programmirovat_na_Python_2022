# Тестовая программа, использующая счета
# Версия 3 с использованием словаря счетов

from Account import *

accountsDict = {}
nextAccountNumber = 0

oAccount = Account('Joe', 100, 'JoesPassword')
joesAccountNumber = nextAccountNumber
accountsDict[joesAccountNumber] = oAccount
print("Joe's account number is 0")
nextAccountNumber += 1

oAccount = Account('Mary', 12345, 'MarysPassword')
marysAccountNumber = nextAccountNumber
accountsDict[nextAccountNumber] = oAccount
print("Mary's account number is 1")

accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()
print()

# вызываем разные методы для разных счетов
print('Calling methods of the two accounts ...')
accountsDict[joesAccountNumber].deposit(50, 'JoesPassword')
accountsDict[marysAccountNumber].withdraw(345, 'MarysPassword')
accountsDict[marysAccountNumber].deposit(100, 'MarysPassword')

# отображаем счета
accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()

# создаем новый счет с информацией от пользователя
print()

userName = input('What is the name for the new user account? ')
userBalance = input('What is the starting balance for this account? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account? ')

nextAccountNumber += 1
newAccountNumber = nextAccountNumber
oAccount = Account(name=userName, balance=userBalance, password=userPassword)

accountsDict[newAccountNumber] = oAccount

# отображаем вновь созданный счет пользователя
print('Created new account, account number is 2')
accountsDict[newAccountNumber].show()

# вносим 100 на новый счет
accountsDict[newAccountNumber].deposit(100, userPassword)
usersBalance = accountsDict[newAccountNumber].getBalance(userPassword)
print()
print("After depositing 100, the user's balance is:", usersBalance)
# отображаем новый счет
accountsDict[newAccountNumber].show()
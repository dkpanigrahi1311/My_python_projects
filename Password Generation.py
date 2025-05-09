
import random
small_letters = 'abcdefghijklmnopqrstuvwxyz'
capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%^&*,./;\=-<>?:{}|+_"'
numbers = '1234567890'
list_capital_letters = list(capital_letters)
list_small_letters = list(small_letters)
list_symbols = list(symbols)
list_numbers = list(numbers)
# Here is questions given below
Q_1 = int(input("How many capital letters do you want? "))
Q_2 = int(input("How many small letters do you want? "))
Q_3 = int(input("How many symbols do you want? "))
Q_4 = int(input("How many numbers do you want? "))
password = ""
for i in range(0, Q_1):
    password += random.choice(list_capital_letters)
for i in range(0, Q_2):
    password += random.choice(list_small_letters)
for i in range(0,Q_3):
    password += random.choice(list_symbols)
for i in range(0, Q_4):
    password += random.choice(list_numbers)
print(password)
list_password = list(password)
random.shuffle(list_password)
new_password = ""
for i in list_password :
    new_password += i
print(new_password)

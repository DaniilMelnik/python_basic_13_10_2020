"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
"""

user_number = input("введите число:")
user_number = int(user_number)
biggest_number = 0
calculated_number = user_number%10
while(user_number != 0):
    if (calculated_number > biggest_number):
        biggest_number = calculated_number
    user_number = (int((user_number - calculated_number)/10))
    calculated_number = user_number % 10

print("Наибольшее число:", biggest_number)

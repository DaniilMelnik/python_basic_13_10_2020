"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
def division(x, y):
    return int(x) / int(y)

user_data = input("Введите два числа через запятую:")
user_list = user_data.split(',')
try:
    print(division(user_list[0],user_list[1]))
except ZeroDivisionError:
    print("Деление на 0")
except:
    print("Некорретный ввод")


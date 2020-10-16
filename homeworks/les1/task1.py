"""
Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""

int_variable = 8
float_variable = 10.1
str_variable = "some_text"

print("int_variable:", int_variable)
print("float_variable:", float_variable)
print("str_variable:", str_variable)

name = input("введите имя пользователя: /n >>>")
number1 = input("введите первое число: /n >>>")
number2 = input("введите второе число: /n >>>")
sum = int(number1) + int(number2)
print("имя пользователя:", name)
print("сумма чисел:", sum)

"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""

def my_func(x, y):
    return x ** y

def my_func_v2(x, y):
    result = x
    while y < -1:
        result *= x
        y += 1
    return 1/result

print(my_func(4.23,-1))
print(my_func_v2(4.23,-1))
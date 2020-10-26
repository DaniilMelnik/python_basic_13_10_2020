"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce

def my_reduce(func, iterable):
    result = iterable[0]
    for el in range(1, len(iterable)):
        result = func(result, iterable[el])
    return result


print([i for i in range(2, 11, 2)])
multiple_all = my_reduce(lambda x, y: x * y, [i for i in range(100, 1001, 2)])
print(multiple_all)

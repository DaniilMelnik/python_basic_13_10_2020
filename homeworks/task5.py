"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce

def my_reduce(func, iterable):
    result = iterable[0]
    #print(result)
    for key, val in enumerate(iterable):
        print(val)
        result = func(result, val)
    return result


#multiple_all = reduce(lambda x, y: x * y, [i for i in range(2, 11, 2)])
#print([i for i in range(2,11,2)])
#print(multiple_all)
print([i for i in range(2, 11, 2)])
multiple_all_my = my_reduce(lambda x, y: x * y, [i for i in range(2, 11, 2)])
print(multiple_all_my)

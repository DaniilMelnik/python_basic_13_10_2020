"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from itertools import (
    count,
    cycle
)

def my_count(start):
    while True:
        yield start
        start += 1

def my_cycle(iterable):
    while True:
        for el in iterable:
            yield el

for el in my_count(3):
    if el > 10:
        print('\nnext script:')
        break
    else:
        print(el)

initial_list = [3, 5, 10, 21]
end_flag = 2 * len(initial_list)
for el in my_cycle(initial_list):
    if end_flag == 0:
        break
    else:
        print(el)
    end_flag -= 1

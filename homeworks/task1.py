"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, Output_in_hour, rate_per_hour, bonus = argv
data = Output_in_hour, rate_per_hour, bonus
try:
    Output_in_hour, rate_per_hour, bonus = list(map(float,data))
except:
    print("Введены некорректные данные")
else:
    print("Заработная плата сотрудника составляет: ", (Output_in_hour * rate_per_hour) + bonus)
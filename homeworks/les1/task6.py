"""
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
"""
a = input("введите результат спортсмена:")
a = float(a)
b = input("введите необходимый результат спортсмена:")
b = float(b)
num_days = 0
while (a <= b):
    a = a + a * 0.1
    num_days = num_days + 1
print("Число дней необходимых для достижения результата:", num_days)

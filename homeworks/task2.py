"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""

def output(**kwargs):
    for key, value in kwargs.items():
        print(key, ': ', value,sep='',end=' | ')

output(имя='Иван',Фамилия='Иванович',год_рождения=1900, город_проживания='Иваново', email='IvanovIvan@mail.ru',телефон='89876543210')
"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""

def show_user_data(name, surname, birth_year, sity, e_mail, phone):
    """
    Вывод данных о пользователе, функция принимает именованные параметры
    """
    print(f"name = {name}, surname = {surname}, birth_year = {birth_year}, sity = {sity}, e_mail = {e_mail}, naphoneme = {phone}")

show_user_data(surname='Иванович',name='Иван',birth_year=1900, sity='Иваново', e_mail='IvanovIvan@mail.ru',phone='89876543210')
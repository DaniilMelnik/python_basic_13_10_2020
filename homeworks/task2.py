"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class My_except(Exception):
    def __init__(self, txt):
        print("in My_except")
        self.txt = txt

while True:
    user_data = input("Введите делитель числа 3 (q для выхода): ")
    if user_data == 'q':
        break
    try:
        if int(user_data) == 0:
            raise My_except("Деление на 0")
        result = 3/int(user_data)
    except ZeroDivisionError:
        print("standert ZeroDivisionError")
        break
    except My_except as err:
        print(err)
    except ValueError:
        pass
    else:
        print(result)

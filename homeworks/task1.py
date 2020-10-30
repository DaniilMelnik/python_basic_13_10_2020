"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

file = open(r'files\user_input_task1.txt', 'w', encoding='UTF-8')

while True:
    user_data = input("Введите необходимую инфомрацию: ")
    if not user_data:
        break
    try:
        file.write(user_data + '\n')
    except:
        print("Ошибка записи файла")
        break
file.close()


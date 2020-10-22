"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""
# решение в лоб
sum_var = 0
output = False
while True:
    user_data = input("Введите числа разделенный проблом(q для выхода): ")
    data_list = user_data.split(' ')
    for el in data_list:
        if el == 'q':
            output = True
            break
        else:
            try:
                sum_var += int(el)
            except:
                pass
    print("Общая сумма: ", sum_var)
    if output == True:
        break




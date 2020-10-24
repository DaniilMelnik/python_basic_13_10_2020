"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

def my_map(func, iterable):
    for el in iterable:
        yield func(el)

def my_sum(iterable):
    sum_val = 0
    for el in iterable:
        sum_val += el
    return sum_val


sum_all = 0
while True:
    user_data = input("Введите числа разделенные пробелом(q для выхода): ")
    data_list = user_data.split(' ')
    if 'q' in data_list:
        q_index = data_list.index('q')
        try:
            sum_all += my_sum(list(my_map(int,data_list[:q_index])))
        except:
            print("Введен недопустимый символ")
            break
        print(sum_all)
        break
    try:
        sum_all += my_sum(list(my_map(int,data_list)))
    except:
        print("Введен недопустимый символ")
        break
    print(sum_all)

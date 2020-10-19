"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

user_list = []
while True:
    user_var = input("Введите элемент списка (""q"" для выхода):")
    if(user_var == 'q'):
        break
    user_list.append(user_var)
print("Оригинальный список:", user_list)

new_list = []
for index in range(0, len(user_list), 2):
    tmp_list = user_list[index:index+2]
    tmp_list.reverse()
    new_list.append(tmp_list)
new_list = sum(new_list, [])
print("Измененный список:", new_list)

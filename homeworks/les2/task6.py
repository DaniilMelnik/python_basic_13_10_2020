"""
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
items = []
item_data = {"название": "", "цена": "", "количество": "", "eд": ""}
item_number = 0
while True:  # Заполнение данных
    item_data["название"] = input("Введите название товара: ")
    item_data["цена"] = input("Введите цену товаров: ")
    item_data["количество"] = input("Введите количество товаров: ")
    item_data["eд"] = input("Введите единицу измерения товара: ")
    item_number += 1
    items.append((item_number, item_data))
    user_choice = input("Нажмите любую клваишу для продолжения (q) для выхода: ")
    if user_choice == 'q':
        break

print("Данные по товарам:")
for item in items:
    print(item)

item_analytics = item_data

for key in item_data.keys():  # Сбор аналитики
    tmp_list = []
    for item in items:
        tmp_list.append(item[1][key])
    item_analytics[key] = tmp_list
    #item_data["цена"] = item[1]["цена"]
    #item_data["количество"] = item[1]["количество"]
    #item_data["eд"] = item[1]["eд"]

print("аналитика по товарам:")
for item in item_analytics:
    print(item)
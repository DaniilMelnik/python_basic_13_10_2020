"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
en_ru_dict = {'One': 'Один', 'Two': 'Два','Three': 'Три', 'Four': 'Четыре'}
file_data = ''
with open(r'files\data_task4.txt', 'r', encoding='UTF-8') as input_file:
    file_data = input_file.read()
    for key, val in en_ru_dict.items():
        file_data = file_data.replace(key, val)
with open(r'files\task4_output.txt', 'w', encoding='UTF-8') as output_file:
    print(file_data,file=output_file)


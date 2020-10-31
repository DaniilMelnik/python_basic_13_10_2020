"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
"""

file = open(r'files\data_task2.txt', 'r', encoding='UTF-8')
strings_num = 0
words_in_line = {}
for line in file:
    words = line.split(' ')
    words_in_line['строка ' + str(strings_num)] = len(words)
    strings_num += 1
print("Количетво строк в файле:", strings_num)
print("Количество слов в строках:")
print(words_in_line)
file.close()

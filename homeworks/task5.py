"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open(r'files\data_task5.txt', 'w+', encoding='UTF-8') as file:
    data_list = [1.2, 22, 3.3, 43.2, 5, 6]
    print(*data_list, file=file, sep=' ')
    file.seek(0)
    for line in file:
        num_in_file = [float(x) for x in line.split(' ')]
        print(sum(num_in_file))

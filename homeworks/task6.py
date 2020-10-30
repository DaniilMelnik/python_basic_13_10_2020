"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
def sum_hours(list):
    all = 0
    for el in list:
        if el.isdigit():
            all += sum
        return all


with open(r'files\data_task6.txt', 'r', encoding='UTF-8') as file:
    data_dict = {}
    for line in file:
        key, lect, pract, lab, = line.rstrip().split(' ')
        data_list = [lect.replace('(л)',''), pract.replace('(пр)',''), lab.replace('(лаб)','')]
        my_sum = sum_hours(data_list)
        #data_dict[key] = sum([float(lect),float(pract),float(lab)])
        print(data_list)
        print(my_sum)
    # for key, val in data_dict.items():
    #     print(val)


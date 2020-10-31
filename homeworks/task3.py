"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""
def mean_salary(dict):
    if dict:
        average = 0
        for el in dict.values():
            average += el
        average = average/len(dict)
        return average


with open(r'files\data_task3.txt', 'r', encoding='UTF-8') as file:
    workers_profit = {}
    for line in file:
        data_list = line.rstrip().split(' ')
        try:
            workers_profit[data_list[0]] = float(data_list[1])
        except ValueError:
            print("некорректные данные об окладе")
            workers_profit.clear()
            break

    for surname, profit in workers_profit.items():
        if profit < 20000:
            print(surname, "имеет доход менее 20000: ", profit)
    print('Средний доход сотрудников: ', mean_salary(workers_profit))

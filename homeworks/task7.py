"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

def calc_average_profit(profit):
    profit_list = [x for x in profit.values() if x > 0]
    try:
        average = sum(profit_list)/len(profit_list)
        return average
    except:
        print("прибыль отсутствует")
        return None

with open(r'files\data_task7.txt', 'r', encoding='UTF-8') as file:
    profits = {}
    average_profit = {}
    for line in file:
        name, form, revenue, cost = line.split(' ')
        profit = float(revenue) - float(cost)
        profits[name] = profit
    average_profit["average_profit"] = calc_average_profit(profits)
    output_list = [profits, average_profit]

with open(r'files\task7_output.txt', 'w', encoding='UTF-8') as output_file:
    json.dump(output_list, output_file)


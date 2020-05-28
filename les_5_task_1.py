# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

number_enterprises = int(input('Введите количество предприятий: '))
enterprises = defaultdict(list)
for i in range(number_enterprises):
    name_enterprise = input('Введите название предприятия: ')
    for j in range(4):
        profit = float(input(f'Введите прибыль за {j + 1}-й квартал: '))
        enterprises[name_enterprise].append(profit)
    enterprises[name_enterprise].append(sum(enterprises[name_enterprise]))

average_profit = 0
for value in enterprises.values():
    average_profit += value[4]
average_profit /= number_enterprises

print('Предприятия с прибылью выше среднего:')
for key, value in enterprises.items():
    if value[4] > average_profit:
        print(key)

print('Предприятия с прибылью ниже среднего:')
for key, value in enterprises.items():
    if value[4] < average_profit:
        print(key)
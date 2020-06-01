# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
    # Определить, какое число в массиве встречается чаще всего.

import random
import sys


def my_show(object):
    size_object = sys.getsizeof(object)
    if hasattr(object, '__iter__'):
        if hasattr(object, 'items'):
            for key, value in object.items():
                size_object += sys.getsizeof(key)
                size_object += sys.getsizeof(value)
        elif not isinstance(object, str):
            for item in object:
                size_object += sys.getsizeof(item)
    return size_object


SIZE = 100
MIN_ITEM = 1
MAX_ITEM = 15
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# Вариант 1
counts = dict()
for i in array:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1
print(counts)

max_item = 0
max_ = 0
for key, item in counts.items():
    if item > max_:
        max_item = key
        max_ = item

print(f'Чаще всего встречается число {max_item}')
size_variant_1 = my_show(array) + my_show(counts) + my_show(i) + my_show(max_item) + my_show(max_) + my_show(key) + my_show(item)
print(f'Выделено памяти (1-й вариант): {size_variant_1}')  # Выделено памяти (1-й вариант): 2686

# Вариант 2
max_item_2 = array[0]
max_2 = 1
for i in range(len(array)):
    count_temp = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            count_temp += 1
    if count_temp > max_2:
        max_2 = count_temp
        max_item_2 = array[i]

print(f'Чаще всего встречается число {max_item_2}')
size_variant_2 = my_show(array) + my_show(max_item_2) + my_show(max_2) + my_show(i) + my_show(count_temp) + my_show(j)
print(f'Выделено памяти (2-й вариант): {size_variant_2}')  # Выделено памяти (2-й вариант): 1922

# Вариант 3
max_item_3 = array[0]
max_3 = 1
for i in range(len(array)):
    if array.count(array[i]) > max_3:
        max_3 = array.count(array[i])
        max_item_3 = array[i]

print(f'Чаще всего встречается число {max_item_3}')
size_variant_3 = my_show(array) + my_show(max_item_3) + my_show(max_3) + my_show(i)
print(f'Выделено памяти (3-й вариант): {size_variant_3}')  # Выделено памяти (3-й вариант): 1894

# Python 3.8 32-bit, Windows 10 x64
# Оптимальным является вариант с наименьшим значением выделенной памяти т.е. №3.

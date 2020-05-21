# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_index = 0
for i in range(len(array)):
    if array[i] < array[min_index]:
        min_index = i

min2_index = 0
for i in range(len(array)):
    if array[i] < array[min2_index] and i != min_index:
        min2_index = i
print(f'Два наименших элемента:\n\t {min_index}-й = {array[min_index]}\n\t {min2_index}-й = {array[min2_index]}')

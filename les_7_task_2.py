# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

from random import uniform


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        arr_1 = arr[0: len(arr) // 2]
        arr_2 = arr[len(arr) // 2: len(arr)]
        return merge(merge_sort(arr_1), merge_sort(arr_2))


def merge(arr_1, arr_2):
    result = []
    i = 0
    j = 0
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] <= arr_2[j]:
            result.append(arr_1[i])
            i += 1
        else:
            result.append(arr_2[j])
            j += 1
    while i < len(arr_1):
        result.append(arr_1[i])
        i += 1
    while j < len(arr_2):
        result.append(arr_2[j])
        j += 1
    return result


MIN = 0
MAX = 49.999
SIZE = 7
array = [uniform(MIN, MAX) for _ in range(SIZE)]
print('Исходный массив:')
print(array)

print('Отсортированный массив:')
print(merge_sort(array))

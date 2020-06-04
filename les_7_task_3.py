# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).
from random import randint


def my(arr):
    less = 0
    more = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] >= arr[j]:
                more += 1
            if i != j and arr[i] <= arr[j]:
                less += 1
            if more >= m and less >= m:
                return arr[i]
        less = 0
        more = 0


MIN = 0
MAX = 10
m = int(input('Введите целое число: '))
size = 2 * m + 1
array = [randint(MIN, MAX) for _ in range(size)]
print('Исходный массив:')
print(array)
#print(sorted(array))

print(f'Медиана: {my(array)}')

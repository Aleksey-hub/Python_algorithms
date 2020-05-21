# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE_A = 7
SIZE_B = 5
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_B)] for _ in range(SIZE_A)]
print(*matrix, sep='\n')

min_elements = matrix[0]
for i in range(SIZE_A):
    for j in range(SIZE_B):
        if matrix[i][j] < min_elements[j]:
            min_elements[j] = matrix[i][j]
print(f'Минимальные значения столбцов:\n{min_elements}')

max_index = 0
for i in range(len(min_elements)):
    if min_elements[i] > min_elements[max_index]:
        max_index = i
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {min_elements[max_index]}')

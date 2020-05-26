# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

import timeit
import cProfile
import sys


# Вариант 1
def sum_series(n):
    if n >= 1:
        result = 0
        k = 1
        for i in range(n):
            result = result + k / 2 ** i
            k = k * -1
        return result
    else:
        print('Необходимо ввести натуральное число.')


print(timeit.timeit('sum_series(10)', number=1000, globals=globals()))  # 0.0057918
print(timeit.timeit('sum_series(100)', number=1000, globals=globals()))  # 0.13220369999999998
print(timeit.timeit('sum_series(1000)', number=1000, globals=globals()))  # 3.5563129
print(timeit.timeit('sum_series(3000)', number=1000, globals=globals()))  # 25.405357600000002

cProfile.run('sum_series(10)')
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:9(sum_series)
cProfile.run('sum_series(100)')
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:9(sum_series)
cProfile.run('sum_series(1000)')
# 1    0.003    0.003    0.003    0.003 les_4_task_1.py:9(sum_series)
cProfile.run('sum_series(3000)')
# 1    0.025    0.025    0.025    0.025 les_4_task_1.py:9(sum_series)


# Вариант 2
def sum_series_2(n):
    return 1 * (1 - (-0.5) ** n) / (1 - (-0.5))


print('*' * 50)
print(timeit.timeit('sum_series_2(10)', number=1000, globals=globals()))  # 0.0007248999999980299
print(timeit.timeit('sum_series_2(100)', number=1000, globals=globals()))  # 0.0007000000000019213
print(timeit.timeit('sum_series_2(1000)', number=1000, globals=globals()))  # 0.0007110000000025707
print(timeit.timeit('sum_series_2(3000)', number=1000, globals=globals()))  # 0.0007286999999998045

cProfile.run('sum_series_2(10)')
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:33(sum_series_2)
cProfile.run('sum_series_2(100)')
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:33(sum_series_2)
cProfile.run('sum_series_2(1000)')
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:33(sum_series_2)
cProfile.run('sum_series_2(3000)')
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:33(sum_series_2)

# Вариант 3
sys.setrecursionlimit(10000)


def sum_series_3(n):
    if n == 1:
        return 1
    if n > 1:
        return sum_series_3(n - 1) + (-1) ** (n - 1) / 2 ** (n - 1)


print('*' * 50)
print(timeit.timeit('sum_series_3(10)', number=1000, globals=globals()))  # 0.011625699999999739
print(timeit.timeit('sum_series_3(100)', number=1000, globals=globals()))  # 0.18844259999999835
print(timeit.timeit('sum_series_3(1000)', number=1000, globals=globals()))  # 4.3173952
print(timeit.timeit('sum_series_3(3000)', number=1000, globals=globals()))  # 28.5439438

cProfile.run('sum_series_3(10)')
# 10/1    0.000    0.000    0.000    0.000 les_4_task_1.py:49(sum_series_3)
cProfile.run('sum_series_3(100)')
# 100/1    0.000    0.000    0.000    0.000 les_4_task_1.py:49(sum_series_3)
cProfile.run('sum_series_3(1000)')
# 1000/1    0.005    0.000    0.005    0.005 les_4_task_1.py:49(sum_series_3)
cProfile.run('sum_series_3(3000)')
# 3000/1    0.029    0.000    0.029    0.029 les_4_task_1.py:49(sum_series_3)

# Оптимальный в данном случае будет вариант №2, т.к. время выполнения минимально
# + не зависит от n (что дает существенный прирост производительности при больших значениях n)

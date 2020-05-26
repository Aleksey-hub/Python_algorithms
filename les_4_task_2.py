# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код
# и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
#
# sieve(2)
# 3
# prime(4)
# 7
# sieve(5)
# 11
# prime(1)
# 2

import timeit
import cProfile


# 1. с помощью алгоритма «Решето Эратосфена»
def sieve(num):
    if num <= 4:
        n = 10
    elif num <= 25:
        n = 4 * num
    elif num <= 168:
        n = 6 * num
    elif num <= 1229:
        n = 9 * num
    else:
        print('Введите порядковый номер простого числа <= 1229.')

    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    return res[num - 1]


# print(sieve(2))
print(timeit.timeit('sieve(1)', number=1000, globals=globals()))  # 0.009206799999999994
print(timeit.timeit('sieve(10)', number=1000, globals=globals()))  # 0.022638599999999995
print(timeit.timeit('sieve(100)', number=1000, globals=globals()))  # 0.5251604
print(timeit.timeit('sieve(1000)', number=1000, globals=globals()))  # 8.5329038

cProfile.run('sieve(1)')
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:26(sieve)
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:38(<listcomp>)
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:48(<listcomp>)
cProfile.run('sieve(10)')
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:26(sieve)
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:38(<listcomp>)
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:48(<listcomp>)
cProfile.run('sieve(100)')
# 1    0.000    0.000    0.001    0.001 les_4_task_2.py:26(sieve)
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:38(<listcomp>)
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:48(<listcomp>)
cProfile.run('sieve(1000)')
# 1    0.008    0.008    0.010    0.010 les_4_task_2.py:26(sieve)
# 1    0.001    0.001    0.001    0.001 les_4_task_2.py:38(<listcomp>)
# 1    0.001    0.001    0.001    0.001 les_4_task_2.py:48(<listcomp>)

# 2. без использования «Решета Эратосфена»
def prime(num):
    if num <= 4:
        n = 10
    elif num <= 25:
        n = 4 * num
    elif num <= 168:
        n = 6 * num
    elif num <= 1229:
        n = 9 * num
    else:
        print('Введите порядковый номер простого числа <= 1229.')

    res = [2, 3]
    for i in range(4, n):
        j = 2
        while j <= int(i ** 0.5):
            if i % j == 0:
                break
            j += 1
        else:
            res.append(i)
    return res[num - 1]


print('*' * 50)
print(timeit.timeit('prime(1)', number=1000, globals=globals()))  # 0.007370399999999222
print(timeit.timeit('prime(10)', number=1000, globals=globals()))  # 0.06395359999999961
print(timeit.timeit('prime(100)', number=1000, globals=globals()))  # 2.6297317000000007
print(timeit.timeit('prime(1000)', number=1000, globals=globals()))  # 103.9453778

cProfile.run('prime(1)')
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:76(prime)
# 2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('prime(10)')
# 1     0.000    0.000    0.000    0.000 les_4_task_2.py:76(prime)
# 10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('prime(100)')
# 1      0.002    0.002    0.002    0.002 les_4_task_2.py:76(prime)
# 107    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('prime(1000)')
# 1       0.097    0.097    0.097    0.097 les_4_task_2.py:76(prime)
# 1115    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

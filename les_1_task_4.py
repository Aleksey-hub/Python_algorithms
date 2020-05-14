# Написать программу, которая генерирует в указанных пользователем границах:
# ● случайное целое число,
# ● случайное вещественное число,
# ● случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

a_int = int(input("Введите a_int: "))
b_int = int(input("Введите b_int: "))
a_float = float(input("Введите a_float: "))
b_float = float(input("Введите b_float: "))
a_alphabet = input("Введите a_alphabet: ")
b_alphabet = input("Введите b_alphabet: ")

int_rand = random.randint(a_int, b_int)
float_rand = random.uniform(a_float, b_float)
alphabet_rand = chr(random.randint(ord(a_alphabet), ord(b_alphabet)))

print(f'{int_rand=}\n{float_rand=}\n{alphabet_rand=}')
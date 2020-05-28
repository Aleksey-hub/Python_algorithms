# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как коллекция,
# элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque


def sum_hex(digit_1, digit_2, prev_digit=0):
    hex_ = tuple('0123456789ABCDEF')
    digit_1_idx = hex_.index(digit_1)
    digit_2_idx = hex_.index(digit_2)
    sum_idx = digit_1_idx + digit_2_idx + prev_digit
    next_digit = sum_idx // 16
    sum_idx %= 16
    sum_ = hex_[sum_idx]
    return sum_, next_digit


def multiplication_hex(num_1, num_2):
    hex_ = tuple('0123456789ABCDEF')

    for i in range(len(num_1)):
        num_1[i] = hex_.index(num_1[i])
    for i in range(len(num_2)):
        num_2[i] = hex_.index(num_2[i])


num_1_hex = list(str.upper(input('Введите первое число: ')))
num_2_hex = list(str.upper(input('Введите второе число: ')))

result_sum = deque()
next_digit = 0
for i in range(1, max(len(num_1_hex), len(num_2_hex)) + 1):
    sum_, next_digit = sum_hex(
        num_1_hex[-i] if i <= len(num_1_hex) else '0',
        num_2_hex[-i] if i <= len(num_2_hex) else '0',
        next_digit)
    result_sum.appendleft(sum_)

print(f'Сумма равна: {result_sum}')

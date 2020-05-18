# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

def num_inverse(num):
    if num // 10 == 0:
        return f'{num}'
    else:
        return f'{num % 10}{num_inverse(num // 10)}'


num_1 = int(input('Введите число: '))
num_result = int(num_inverse(num_1))
print(num_result)
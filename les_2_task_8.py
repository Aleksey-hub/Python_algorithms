#  Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
#  Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

count_number = int(input('Введите количество вводимых чисел: '))
search_digit = int(input('Введите искомую цифру: '))

count_digit = 0
for i in range(1, count_number + 1):
    number_temp = int(input(f'Введите {i}-е число: '))
    while number_temp != 0:
        digit_temp = number_temp % 10
        if digit_temp == search_digit:
            count_digit += 1
        number_temp = number_temp // 10

print(f'Цифра {search_digit} встречается {count_digit} раз(а)')
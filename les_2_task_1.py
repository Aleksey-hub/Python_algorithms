#  Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
#  Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
#  а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
#  в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
#  программа должна сообщать об ошибке и снова запрашивать знак операции.
#  Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

# https://drive.google.com/file/d/1IuFh61CNGhQq9Hs1vJHzqAM9ilv1bqOY/view?usp=sharing

while True:
    num_1 = float(input('Введите первое число: '))
    num_2 = float(input('Введите второе число: '))
    operation = input('Введите знак операции (для выхода введите "0"): ')
    if operation == '/':
        if num_2 == 0:
            print('На ноль делить нельзя.')
            continue
        else:
            result = num_1 / num_2
            print(result)
            continue
    elif operation == '*':
        result = num_1 * num_2
        print(result)
        continue
    elif operation == '-':
        result = num_1 - num_2
        print(result)
        continue
    elif operation == '+':
        result = num_1 + num_2
        print(result)
        continue
    elif operation == '0':
        break
    else:
        print('Неверный знак операции')
        continue


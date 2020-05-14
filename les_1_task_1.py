# https://drive.google.com/file/d/1jYgILl-oK5a3T81sdHka65cXSwgE0FHo/view?usp=sharing
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = int(input('Введите трехзначное число: '))

num_3 = a // 100
num_2 = (a - num_3 * 100) // 10
num_1 = a - num_3 * 100 - num_2 * 10

sum = num_1 + num_2 + num_3
mult = num_1 * num_2 * num_3

print(f'{sum=}\n{mult=}')

# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

counts = dict()
for i in range(2, 10):
    counts[i] = 0
print(counts)

for key in counts:
    for i in range(2, 100):
        if i % key == 0:
            counts[key] += 1
print(counts)

size = int(input('Введите длину последовательности: '))
count = 0
for _ in range(size):
    division_counter = 0
    num = int(input('Введите число: '))
    for j in range(1, num+1):
        if num % j == 0:
            division_counter += 1
    if division_counter > 2:
        division_counter = 0
    else:
        count += 1

print(f'Количество простых чисел в последовательности {count}')
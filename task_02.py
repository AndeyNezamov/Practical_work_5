number = int(input('Введите число: '))
for i in range(1, number + 1):
    for _ in range(i):
        print(f'{i}', end='\t')
    print()

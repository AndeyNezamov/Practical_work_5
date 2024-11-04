size = int(input('Введите размер матрицы: '))
for i in range(size + 1):
    for j in range(size + 1):
        print(i + j * 2, end='\t')
    print()
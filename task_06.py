number = int(input('Введите число: '))
for i in range(number):
    print(' ' * (number - i - 1) + '#' * (i * 2 + 1))
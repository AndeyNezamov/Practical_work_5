x_lim = int(input('Введите высоту: '))
y_lim = int(input('Введите длину'))

for y in range(y_lim):
    for x in range(x_lim):
        if x == 0 or x == x_lim - 1:
            print('|', end='')
        elif y == 0 or y == y_lim - 1 :
            print('-', end='')
        else:
            print(' ', end='')
    print()

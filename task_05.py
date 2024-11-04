numbers = int(input('Введите количество чисел: '))
max_num = 0
max_summ = 0
for i in range(numbers):
    num = int(input('ведите число: '))
    res = 0
    temp = num
    while temp > 0:
        res += temp % 10
        temp //= 10

    if res > max_summ:
        max_summ = res
        max_num = num
print(f'Число {max_num} имеет максимальную сумму цифр: {max_summ}')
def Binarne(value):
    count = 0
    result = 0
    for i in range(len(str(value)) - 1, -1, -1):
        result += int(str(value)[count]) * (2 ** i)
        count += 1
        if count >= len(str(value)):
            break
    print(f'Число {value} было переведено в десятичную систему счисления: {result}')

Binarne(int(input('Введите число, которое хотите перевести в десятичную систему счисления: ')))













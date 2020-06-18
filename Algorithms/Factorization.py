def get_dividers(a):
    a = abs(a)
    dividers = []
    divider = 2
    while a != 1:
        while a % divider == 0:
            dividers.append(divider)
            a //= divider
        divider += 1
    return dividers


print('Разложение числа а на простые множители:')
print('a = ')
a = int(input())
print(get_dividers(a))

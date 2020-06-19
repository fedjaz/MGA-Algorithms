def get_dividers(a):
    a = abs(a)
    dividers = {}
    divider = 2
    while a != 1:
        while a % divider == 0:
            if divider in dividers:
                dividers[divider] += 1
            else:
                dividers[divider] = 1
            a //= divider
        divider += 1
    return dividers


print('Разложение числа а на простые множители:')
print('a = ')
a = int(input())
dividers = get_dividers(a)
s = [(str(key) if value == 1 else '%d^%d' % (key, value)) for (key, value) in dividers.items()]
print(' * '.join(s))

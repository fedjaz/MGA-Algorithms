print('Разложение вида a = bq + r:')
print('a = ')
a = int(input())
print('b = ')
b = int(input())
if b == 0:
    print('b не может принимать отрицательное значение')
    exit()
q = int(a / b)
r = a - b * q
print('%d = %d * %d + %d' % (a, b, q, r))

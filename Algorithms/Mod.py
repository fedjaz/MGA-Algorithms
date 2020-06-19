print('Разложение вида a = bq + r:')
print('a = ')
a = int(input())
print('b = ')
b = int(input())
if b == 0:
    print('b не может принимать нулевое значение')
    exit()
r = a % b
if r < 0:
    r += abs(b)
q = (a - r) / b
print('%d = %d * %d + %d' % (a, b, q, r))

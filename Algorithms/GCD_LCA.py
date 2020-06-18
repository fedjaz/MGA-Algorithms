def gcd(a, b):
    (a, b) = (abs(a), abs(b))
    if a > b:
        (a, b) = (b, a)
    while b != 0:
        a %= b
        (a, b) = (b, a)
    return a


print('Нахождение НОД и НОК числе а и b:')
print('a = ')
a = int(input())
print('b = ')
b = int(input())
ans = gcd(a, b)
print('НОД = %d' % ans)
print('НОК = %d' % (a * b / ans))

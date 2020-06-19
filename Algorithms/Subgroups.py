def gcd(a, b):
    (a, b) = (abs(a), abs(b))
    if a > b:
        (a, b) = (b, a)
    while b != 0:
        a %= b
        (a, b) = (b, a)
    return a


print('Нахождение подгрупп группы а:')
print('a = ')
a = int(input())
for k in range(1, a + 1):
    if a % k == 0:
        s = "k = %d => " % k
        for i in range(1, a + 1):
            if gcd(a, i) == a // k:
                s += 'e ' if i == a else str(i) + ', '
        print(s)

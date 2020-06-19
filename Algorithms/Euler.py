def phi(n):
    ans = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            ans -= ans / i
        i += 1
    if n > 1:
        ans -= ans / n
    return ans


print('Вычисление функции Эйлера для числа n:')
print('n = ')
n = int(input())
if n < 1:
    print('Число должно быть натуральным')
    exit()
print('фи(%d) = %d' % (n, phi(n)))
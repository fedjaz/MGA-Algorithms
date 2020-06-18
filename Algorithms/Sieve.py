def get_primes_in_range(a, b):
    arr = [False] * (b + 1)
    ans = []
    for i in range(2, b + 1):
        if not arr[i]:
            if i >= a:
                ans.append(i)
            j = 2 * i
            while j <= b:
                arr[j] = True
                j += i
    return ans


print('Нахождение простых чисел между a и b:')
print('a = ')
a = int(input())
print('b = ')
b = int(input())
if a > b or a < 1 or b < 1:
    print('Введенные числа некорректны')
    exit()
print(get_primes_in_range(a, b))

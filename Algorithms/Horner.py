print('Схема Горнера для многочлена s и числа а:')
print('s = ')
s = [int(i) for i in input().split()]
print('a = ')
a = int(input())

ans = [s[0]]
for i in range(1, len(s)):
    ans.append(s[i] + a * ans[i - 1])
print('  ' + ' '.join([str(i) for i in s]))
print(str(a) + ' ' + ' '.join([str(i) for i in ans]))
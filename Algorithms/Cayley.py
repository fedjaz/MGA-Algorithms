print('Таблица Кэли для а:')
a = int(input())
if a < 1:
    print('Введено неверное значение')
    exit()
s = '+ '
for i in range(0, a):
    s += str(i) + ' '
print(s)
for i in range(0, a):
    s = str(i) + ' '
    for j in range(0, a):
        s += str((i + j) % a) + ' '
    print(s)
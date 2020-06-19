def encrypt(s, key):
    s = [(ord(i) - ord('а') if i != ' ' else ord('я') - ord('а') + 1) for i in list(s)]
    for i in range(0, len(s)):
        s[i] = ((s[i] + key) % (ord('я') - ord('а') + 2))
    return ''.join([chr(ord('а') + i) if i != ord('я') - ord('а') + 1 else ' ' for i in s])


print('Зашифровать или расшифровать строку s с ключом key:')
print('s = ')
s = input()
print('key = ')
key = int(input())
print('Зашифрованная строка - %s' % encrypt(s, key))
print('Расшифрованная строка - %s' % encrypt(s, -key))

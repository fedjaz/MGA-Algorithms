def encrypt(s, key, val):
    s = [(ord(i) - ord('а') if i != ' ' else ord('я') - ord('а') + 1) for i in list(s)]
    key = [(ord(i) - ord('а') if i != ' ' else ord('я') - ord('а') + 1) for i in list(key)]
    for i in range(0, len(s)):
        s[i] = ((s[i] + key[i % len(key)] * val) % (ord('я') - ord('а') + 2))
    return ''.join([chr(ord('а') + i) if i != ord('я') - ord('а') + 1 else ' ' for i in s])


print('Шифр Вижинера для строки s и ключа key')
print('s = ')
s = input()
print('key = ')
key = input()
print('Зашифрованная строка - %s' % encrypt(s, key, 1))
print('Расшифрованная строка - %s' % encrypt(s, key, -1))

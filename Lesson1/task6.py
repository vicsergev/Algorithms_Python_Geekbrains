'''
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
'''


num = int(input('Введите номер буквы в алфавите '))

ans = chr(num + 96)

print(f'Это буква {ans}')
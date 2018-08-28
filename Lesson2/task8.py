'''
Посчитать, сколько раз встречается определенная цифра в введенной
последовательности чисел. Количество вводимых чисел и цифра, которую
необходимо посчитать, задаются вводом с клавиатуры.
'''

n = int(input('Введите количество вводимых чисел '))
s = int(input('Введите искомую цифру '))

count = 0

# Первое решение, пришедшее в голову, которое затем было решено заменить

# nums = ''
# for i in range(n):
#     nums += input(f'Введите число номер {i + 1}: ')

# for el in nums:
#     if el == str(s):
#         count += 1

for i in range(n):
    num = int(input(f'Введите число номер {i + 1}: '))

    while num != 0:
        if num % 10 == s:
            count += 1
        num //= 10

print(f'{s} встречается {count} раз')
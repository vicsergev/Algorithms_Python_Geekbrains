'''
Посчитать, сколько раз встречается определенная цифра в введенной
последовательности чисел. Количество вводимых чисел и цифра, которую
необходимо посчитать, задаются вводом с клавиатуры.
'''

n = int(input('Введите количество вводимых чисел '))
s = input('Введите искомую цифру ')

count = 0
nums = ''
for i in range(n):
    nums += input(f'Введите число номер {i + 1}: ')

for el in nums:
    if el == s:
        count += 1

print(f'{s} встречается {count} раз')
import random

command = int(input('Введите номер команды:\n1 - вывести случайное целое число\n2 - случайное вещественное число\n3 - случайный символ\n'))

if command == 1:
	x, y = map(int, input('Введите начало и конец диапазона ').split())
	print(random.randint(x, y))

elif command == 2:
	x, y = map(int, input('Введите начало и конец диапазона ').split())
	print(random.uniform(x, y))

else:
	x, y = map(str, input('Введите начало и конец диапазона ').split())
	x_num = ord(x)
	y_num = ord(y)

	ans_num = random.randint(x_num, y_num)
	ans = chr(ans_num)

	print(ans)
# форматирования строки с помощью метода format()
print('{0} {1} cost per three ${2} {3} {4} {5}'.format(3, "apples", 4, "dollars", 50, "cents"))
print('{} {} cost ${}'.format(6, "bananas", 2.48))
# f строки и работа с ними
apple = 7
greypfrut = 6
watermilow = 2
for i in range(1, 5, 3):
	print(i)
	print(f'{apple}{greypfrut}{watermilow} frutes')
print(f'{apple} please eating {greypfrut} and {watermilow} today')

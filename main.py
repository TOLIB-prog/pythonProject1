# форматирования строки с помощью метода format()
print('{0} {1} cost per three ${2} {3} {4} {5}'.format(3, "apples", 4, "dollars", 50, "cents"))
print('{} {} cost ${}'.format(6, "bananas", 2.48))
# f строки и работа с ними
apple = 7
greypfrut = 6
watermilow = 2
print(f'{apple} please eating {greypfrut} and {watermilow} today')

num = input("Enter a number to be doubled:")
doubled_num = int(num) * 12
print(doubled_num, 'you find your number!')

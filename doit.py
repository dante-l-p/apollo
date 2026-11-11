from random import randrange

def isEven(number):
	return number % 2 == 0

def isOdd(number):
	return not isEven(number)

# main
number = randrange(100)
if isEven (10):
	print(f'{number} is even!')
else:
	print(f'{number} is odd!')

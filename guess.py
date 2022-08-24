#r is the random number
#g is the number user guessed
import random
r = random.randint(1, 100)
while True:
	g = input('Please guess a number:')
	g = int(g)
	if g == r:
		print('Bingo!')
		break
	elif g > r:
		print('Wrong, the number is lower')
	elif g < r:
		print('Wrong, the number is higher')




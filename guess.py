#tell the user the answer is highwe/lower if the user answer wrong
#r is the random number
#g is the number user guessed
import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count =  count + 1
	g = input('Please guess a number:')
	g = int(g)
	if g == r:
		print('Bingo!')
		print('You have guessed', count, 'times') #print times when Bingo
		break
	elif g > r:
		print('Wrong, the number is lower')
	elif g < r:
		print('Wrong, the number is higher')
	print('You have guessed', count, 'times')




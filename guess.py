# tell the user the answer is highwe/lower if the user answer wrong
# add count
# add user decide range

import random
start = input('Please decide the starting number for the range:')
start = int(start)
end = input('Please decide the ending number for the range:')
end = int(end)

r = random.randint(start, end) #r is the random number
count = 0

while True:
	count += 1 # count =  count + 1
	g = input('Please guess a number:') #g is the number user guessed
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




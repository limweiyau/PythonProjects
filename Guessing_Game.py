import random

print("Welcome! This is a guessing game. The program will tell you if you're guessing too high or too low!")

guess = int(input("Enter a number between 1 and 100: "))

random_number = random.randint(1, 100)

while True:
	if guess == random_number:
		print("You Win!")
		break
	else:
		if guess > random_number:
			print("Too high!")
		else:
			print("Too low!")
		guess = int(input("Enter a number between 1 and 100: "))
		

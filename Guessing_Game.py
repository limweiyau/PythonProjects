import random

def get_number():
    '''prompt user for specifically a positive integer'''
    while True:
        try:
            user_input = int(input("Please enter a positive integer between 1 and 100: "))
            if user_input > 0 and user_input < 101:
                return user_input
            else:
                print("The number must be between 1 and 100. Please try again.")
        except ValueError:
            print("That's not an integer. Please try again.")

print("Welcome! This is a guessing game. The program will tell you if you're guessing too high or too low!")

guess = get_number()
 
random_number = random.randint(1, 100)

tries = 10

while True:

	tries -= 1

	if tries == 0:
		print(f"Thank you for playing! Unfortunately, you have no tries left.")
		break
	
	if guess == random_number:
		print(f"You Win! You took {10-tries} tries!")	
		break
	else:
		if guess > random_number:
			print(f"Too high! You have guessed {tries} tries left.")
		else:
			print(f"Too low! You have guessed {tries} tries left.")

		guess = int(input("Enter a number between 1 and 100: "))
		

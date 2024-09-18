number1 = int(input("Enter your first number: "))
operator = input("Enter your operator [+][-][x][/]: ")
number2 = int(input("Enter your second number: "))

if operator == '+':
	print(f"Your result is {number1 + number2}.")
elif operator == '-':
	print(f"Your result is {number1 - number2}.")
elif operator == 'x':
	print(f"Your result is {number1 * number2}.")
elif operator == '/':
	print(f"Your result is {number1 / number2}.")
else:
	print("You did not choose one of the operators stated. Please try again.")

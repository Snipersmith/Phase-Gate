import random

print ("Welcome to my substraction app")
points = 0

for index in range(1, 10):
	first_number = random.randint(0, 100)
	second_number = random.randint(0, 100)

print (f"Question 1 What is {first_number} - {second_number}")

for attempt in range (1, 3):
	answer = int(input("Your answer: "))

	if answer == first_number - second_number:
		print ("correct")
		points = +1

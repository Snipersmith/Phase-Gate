numbers = [4, 9, 25, 49]


def is_perfect_square(number):
	if number < 0:
		return False
	index = 0
	while index * index <= number:
			if index * index == number:
				return True
			index += 1
	return False

def get_perfect_square(numbers):
	result = [None] * len(numbers)
	index = 0
	for number in numbers:
		if is_perfect_square(number):
			result[index] = True
		else:
			result[index] = False
		index += 1
	return result
 	
print(get_perfect_square(numbers))


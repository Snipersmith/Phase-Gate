"""
Pseudo
- Create an empty packing space that can accommodate 20 cars
- Make sure a car can enter this packing lot from left to right
- Make sure a car can leave the packing lot
- Make sure two cars can't be a one packing lot 
- When a car leave the packing lot, Make sure the slot number is specified 
- Display the available space status after each action
- Display the filled space status after each action

"""

parking_lot = [None] * 20


def park_car(car_number):
	for index in range (len(parking_lot)):
		if parking_lot[index] is None:
			parking_lot[index] = car_number
			print(f"Car {car_number} parked at slot {index + 1}. ")
			return

	print("Parking lot is full!")




def remove_car(slot_number):
	index = slot_number -1
	if 0 <= index < len(parking_lot):
		if parking_lot[index] is not None:
			print(f"Car {parking_lot[index]} left slot {slot_number}.")
			parking_lot[index] = None
		
		else:
			print(f"Slot {slot_number} is already empty.")
	else:
		print("Invalid slot number!")


def display_status():
	available = [index + 1 for index, car in enumerate(parking_lot) if car is None]
	filled = [f"Slot {index + 1}: {car}" for index, car in enumerate(parking_lot) if car is not None]

	print("\nAvailable slots:", available)
	print("Filled slots:")
	if filled:
		for status in filled:
			print(status)
	else:
		print("None")
	print()



def main():
	print(">>>> Welcome to Sniper's Parking Lot <<<<\n")

	while True:
		print("1. Park a Car")
		print("2. Remove a Car")
		print("3. Show Parking Status")
		print("4. Exit")

		choice = input("Enter a choice (1-4): ")

		if choice == '1':
			car_number = input("Enter your car number: ")
			park_car(car_number)

		elif choice == '2':
			slot_input = input("Enter slot number to remove car: ")
			if slot_input.isdigit():
				slot = int(slot_input)
				remove_car(slot)
			else:
				print("Invalid input! Enter a number.\n")

		elif choice == '3':
			display_status()

		elif choice == '4':
			print("Goodbye!")
			break

		else:
			print("Invalid choice! Try again.\n")


if _name_ == "_main_":
	main()
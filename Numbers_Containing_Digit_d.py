def has_digit(digit, num):
	if digit in str(num):
		return True
	return False

def find_numbers(digit, number):
	all_nums = []
	for num in range(0, number+1):
		if has_digit(digit, num):
			all_nums.append(num)
	return all_nums

if __name__ == '__main__':
	number = int(input("Enter the number \n"))
	digit = input("Enter the digit \n")

	all_nums = find_numbers(digit, number)
	print(f"The number with the digit {digit} are - {all_nums}" if all_nums else f"There are no numbers that contain digit {digit}")


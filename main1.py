def add(a, b):
	return a + b


def main():
	first_number = int(input("Enter first number: "))
	second_number = int(input("Enter second number: "))
	total = add(first_number, second_number)

	print("First number:", first_number)
	print("Second number:", second_number)
	print("Total:", total)


if __name__ == "__main__":
	main()

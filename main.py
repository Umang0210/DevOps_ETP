def add(a, b):
    return a + b


def main():
    first_number = int(input("Enter the first number: \n"))
    second_number = int(input("Enter the second number: \n"))
    total = add(first_number, second_number)

    print("First Number: ", first_number)
    print("Second Number: ", second_number)
    print("Total: ", total)

if __name__ == "__main__":
    main()
def write_numbers_to_file(filename="numbers.txt"):
    with open(filename, 'w') as file:
        for i in range(10):
            while True:
                try:
                    number = int(input(f"Enter number {i+1}: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number")
            file.write(str(number) + "\n")

write_numbers_to_file()
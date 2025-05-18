n = int(input("Enter the number of elements: "))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
print(f"Sum of all elements: {sum(numbers)}")

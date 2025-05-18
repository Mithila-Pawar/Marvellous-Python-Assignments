n = int(input("Enter the number of elements: "))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
search_num = int(input("Enter the number to search: "))
print(f"Frequency of {search_num}: {numbers.count(search_num)}")

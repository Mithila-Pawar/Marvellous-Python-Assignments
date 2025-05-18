from functools import reduce

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

filtered_numbers = list(filter(lambda x: x < 70, numbers))

mapped_numbers = list(map(lambda x: x + 10, filtered_numbers))

product = reduce(lambda x, y: x * y, mapped_numbers)

print(f"Filtered numbers: {filtered_numbers}")
print(f"Mapped numbers: {mapped_numbers}")
print(f"Product of all numbers: {product}")

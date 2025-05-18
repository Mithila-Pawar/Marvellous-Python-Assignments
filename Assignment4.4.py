from functools import reduce

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

squared_numbers = list(map(lambda x: x ** 2, even_numbers))

sum_of_squares = reduce(lambda x, y: x + y, squared_numbers)

print(f"Even numbers: {even_numbers}")
print(f"Squared numbers: {squared_numbers}")
print(f"Sum of squares: {sum_of_squares}")

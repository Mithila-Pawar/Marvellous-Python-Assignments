def sum_of_factors(n):
    factors = [i for i in range(1, n + 1) if n % i == 0]
    return sum(factors)

num = int(input("Enter a number: "))
print(f"Sum of factors of {num} is {sum_of_factors(num)}")

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter the number of elements: "))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
prime_sum = sum(num for num in numbers if is_prime(num))
print(f"Sum of prime numbers: {prime_sum}")

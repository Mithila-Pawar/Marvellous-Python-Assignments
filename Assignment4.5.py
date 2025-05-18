from functools import reduce

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

prime_numbers = list(filter(is_prime, numbers))

doubled_primes = list(map(lambda x: x * 2, prime_numbers))

max_prime = reduce(lambda x, y: x if x > y else y, doubled_primes)

print(f"Prime numbers: {prime_numbers}")
print(f"Doubled prime numbers: {doubled_primes}")
print(f"Maximum of doubled primes: {max_prime}")

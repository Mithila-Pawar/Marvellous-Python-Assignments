import multiprocessing

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    numbers = [5, 6, 7, 8]
    with multiprocessing.Pool() as pool:
        results = pool.map(factorial, numbers)
        print(results)
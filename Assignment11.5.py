def count_zeros(number):
    zero_count = 0
    number_str = str(number)

    for digit in number_str:
        if digit == '0':
            zero_count += 1

    return zero_count

number = 10204050
zeros = count_zeros(number)
print("Number of zeros:", zeros)
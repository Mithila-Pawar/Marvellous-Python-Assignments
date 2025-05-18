num = int(input("Enter a number: "))
sum_digits = sum(int(digit) for digit in str(abs(num))) 
print(f"Sum of digits: {sum_digits}")

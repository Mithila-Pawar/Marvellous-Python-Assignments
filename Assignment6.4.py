num = int(input("enter a number: "))

fac = 1

for i in range(1, num + 1):
	fac = fac * i

print("factorial of ", num, " is ", fac)
n = int(input("Enter a value for n: "))
for x in range(1, n+1):
    for y in range(n, 0, -1):
        if y > x:
            print(" ", end = "")
        else:
            print("*", end = "")
    print("")
for x in range(1, n):
    for y in range(n):
        if y < x:
            print(" ", end = "")
        else:
            print("*", end = "")
    print("")
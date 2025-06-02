def multiplyNumbers(givenNumbers):
   return givenNumbers*2

givenNumbers = map(multiplyNumbers, [5, 2, 3, 4, 3, 4, 1, 2, 8, 10])
print("Multiplying list elements with 2:")
for element in givenNumbers:
   print(element)
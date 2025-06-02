def sumdigits(number):
  if number==0:
    return 0
  if number!=0:
    return (number%10) + (number//10)
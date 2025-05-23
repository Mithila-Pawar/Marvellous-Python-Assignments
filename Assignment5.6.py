Tc = int(input("Enter a Temperature in Celsius: "))
Tf = ((9 * Tc)/5) + 32
def convert(Tc, Tf):
    print(Tc, "in degrees Celsius is", Tf, "in degrees Fahrenheit")
    return Tf
convert(Tc, Tf)
def C_to_F(Celsius):
    Fahrenheit=9.0/5.0 * Celsius +32
    return Fahrenheit

Celcius = int(input("Enter temperature in Celsius: "))
print(C_to_F(Celcius))


def F_to_C(F):
    Celcius=(F - 32) * 5.0/9.0
    print(Celcius)

F=float(input("Enter temperature in Farenheit?: "))
F_to_C(F)

print("Hello world")

def C_to_F(Celsius):
    Fahrenheit=9.0/5.0 * Celsius +32
    return Fahrenheit

print(C_to_F(9))

def area_circle(radius):
    pi=3.14
    return pi * radius ** 2

print(area_circle(1))

def volume(radius, height):
    pi=3.14159
    v=pi * radius ** 2 * height
    return v

print("volume of cylinder with radius ", 1, " and height 2 is ", volume(1,2))
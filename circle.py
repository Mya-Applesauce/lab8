import math

def area(radius):
    area = math.pi * (radius ** 2)
    print(f"The area of thy circle is {area:.2f}")

area(float(input("Enter the radius of thy circle!")))


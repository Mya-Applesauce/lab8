"""
circle
Ari Papke
circle math
03/23/26
"""

import math

def area(radius):
    area = math.pi * (radius ** 2)
    print(f"The area of the pie is {area:.2f}")

def circumference(radius):
    circumference = 2 * math.pi * radius * 2
    print(f"The circumference of the pie is {circumference:.2f}")


area(float(input("Enter the radius of the pie!")))
circumference(float(input("Enter the radius of the pie!")))
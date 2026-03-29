"""
circle
Ari Papke
circle math
03/23/26
"""

import math

def area(radius):
    area = math.pi * (radius ** 2)
    print(f"The area of the circle is {area:.2f}")

def circumference(radius):
    circumference = 2 * math.pi * radius * 2
    print(f"The circumference of the circle is {circumference:.2f}")

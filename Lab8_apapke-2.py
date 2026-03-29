"""
Lab8_apapke-2
Ari Papke
geometry calcuator
03/29/26
"""

#have to use aliases cause both modules have functions named area.
from circle import area as ca
from circle import circumference as cc
from rectangle import area as ra
from rectangle import perimeter as rp

active = True
while active:
    choice = input((f"Welcome to the Geometry Calcuator!\nThese are the options, choose one... IF YOU DARE!\nPress 1 for the area of a circle.\nPress 2 for the circumference of a circle.\nPress 3 for the area of a rectangle.\nPress 4 for the perimeter of a rectangle.\nPress 5 if you just want to leave."))
    if choice == "1":
        ca(float(input("Enter the radius of the circle.")))
    elif choice == "2":
        cc(float(input("Enter the radius of the circle.")))
    elif choice == "3":
        ra(float(input("Enter the width of the rectangle.")), float(input("Enter the height of the rectangle.")))
    elif choice == "4":
        rp(float(input("Enter the width of the rectangle.")), float(input("Enter the height of the rectangle.")))
    elif choice == "5":
        active = False
    else:
        print("You fool! THAT is not an option! Try again!\n")
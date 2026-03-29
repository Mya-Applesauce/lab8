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
    choice = input((f"Welcome to the geometry calcuator!"))
    if choice == "1":
        ca(float(input()))
    elif choice == "2":
        cc(float(input()))
    elif choice == "3":
        ra(float(input()), float(input()))
    elif choice == "4":
        rp(float(input()), float(input()))
    elif choice == "5":
        active = False
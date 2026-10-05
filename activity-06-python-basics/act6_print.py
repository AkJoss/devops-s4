# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:37:38 2025

@author: josea
"""

# Print author name, then list integers in range(n).
# @author José Alberto Rocha Munguía

print("José Alberto Rocha Munguía")
print("Ingrese un número entero: ")

try:
    n = int(input())
    print("El numero ingresado es:", n)

    for number in range(n):
        print(number)
except Exception:
    print("La entrada no es un entero")

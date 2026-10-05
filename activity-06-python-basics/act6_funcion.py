# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:32:27 2025

@author: josea
"""

# Same logic as act6_print_square, wrapped in a function.
# @author José Alberto Rocha Munguía

def print_funcion():
    for number in range(n):
        if (n % 2) == 0:
            print("El número ingresado es: ", number)
        else:
            print("El cuadrado del número es:", pow(number, 2))


print("Ingrese un número entero: ")
try:
    n = int(input())
    print("El numero ingresado es:", n)
    print_funcion()
except Exception:
    print("La entrada no es un entero")

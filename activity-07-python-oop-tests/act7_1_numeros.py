# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 17:07:21 2025

@author: josea
"""

# Number helpers used by the module demo and unit tests.
# @author José Alberto Rocha Munguía


class Numeros:
    def __init__(self, n):
        self.n = n

    def print_numeros(self):
        for number in range(int(self.n)):
            if (int(self.n) % 2) == 0:
                print("El numero es: ", number)
            else:
                print("El cuadrado del numero es: ", pow(number, 2))


class Racionales(Numeros):
    def __init__(self, n):
        super().__init__(n)

    def print_numeros(self):
        print("El número racional es: ", self.n)
        print("El numero racional en fraccion es: ", float(self.n).as_integer_ratio())

    def print_hello(self):
        # Used by act7_unit_test.py (CI / unittest coursework)
        return "Hello José"

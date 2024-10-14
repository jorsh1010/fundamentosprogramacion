"""
programa3

programa que calcule la hipotenusa de un triangulo

entradas:
ladoa:integer
ladob:integer

salidas:
hipotenusa
"""
import math 

ladoa = input("ingreseel valor de lado A")
ladoa=int(ladoa)
ladob =input("ingrese elvalor de lado B")
ladob = int(ladob)
hipotenusa=ladoa*ladoa+ladob*ladob
hipotenusa=hipotenusa**(1/2)
hipotenusa = math. sqrt(hipotenusa)
print("la hipotenusa es:" , hipotenusa)

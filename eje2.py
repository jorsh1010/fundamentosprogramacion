"""
programa2
crear un programa que calcule el area y perimetro de un rectangulo

Entradas:
base: integer
altura:interger
"""
base = input("ingrese la base")
base = int(base)
altura = input("ingrese la altura")
altura=int(altura)
perimetro= (base+altura)*2
area=base*altura

print(" el area del rectangulo es", area)
print("el perimetro del rectangulo es", perimetro)
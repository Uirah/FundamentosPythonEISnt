import math

a = int(input("Digite o tamanho do primeiro cateto do triangulo: "))
b = int(input("Digite o tamanho do segundo cateto do triangulo: "))
print(f"A hipotenusa desse triangulo mede {math.sqrt(a**2+b**2):.2f}")
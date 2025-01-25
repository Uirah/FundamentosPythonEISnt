# pedir ao utilizador um númeor e devolver a sua raiz quadrada
import math

numero = int(input("Introduza um número inteiro:\n--->"))

quadrado = numero**2

print(f"O quadrado do número é: {quadrado}")

print(f"A raiz quadrada do teu número é {math.sqrt(numero):.3f}")
print(f"A raiz quadrada do teu número arredondada é {round(math.sqrt(numero),4)}")
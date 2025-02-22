'''Crie um programa que captura qualquer erro e exibe uma mensagem
apropriada.'''

import sys

try:
    numero = int(input("Digite um número: "))
    print(f"\nO dobro do número é: {numero * 2}\n")

except Exception as e:
    print(f"Erro inesperado: {e}\n")
    sys.exit()
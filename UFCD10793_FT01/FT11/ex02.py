"""Escreve uma função em Python que, dados a medida do comprimento do lado de
um quadrado imprima os valores do seu perímero e da sua área (area=lado x
lado; perimetro = 4 x lado)."""


def quadrado(lado1):
    area = lado1*lado1
    perimetro = lado1*4
    return print(f"A área do quadrado é {area} \nO perímetro desse quadrado é {perimetro}\n")


print("\033[1;32;40m*********************************\033[m")
print("\033[1;31;40m***** FUNDAMENTOS DE PYTHON *****\033[m")
print("\033[1;32;40m*********************************\033[m\n")

lado1 = int(input("Digite o lado de um quadrado: \n"))


quadrado(lado1)
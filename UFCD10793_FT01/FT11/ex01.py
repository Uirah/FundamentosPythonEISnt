"""Escreve uma função em Python que, dados a medida do comprimento dos três
lados de um triângulo diga se o mesmo é equilátero, isósceles ou escaleno."""



def triangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        print(f"O triângulo é equilátero \n")

    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        print(f"O triângulo é escaleno \n")
        
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print(f"O triângulo é isósceles \n")
        
    else:
        print("Deu ruim")

print("\033[1;32;40m*********************************\033[m")
print("\033[1;31;40m***** FUNDAMENTOS DE PYTHON *****\033[m")
print("\033[1;32;40m*********************************\033[m\n")

lado1 = int(input("Digite lado de um triângulo: "))
lado2= int(input("Digite outro lado de um triângulo: "))
lado3 = int(input("Digite o último lado de um triângulo: "))

triangulo(lado1, lado2, lado3)



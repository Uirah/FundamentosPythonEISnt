
print("\033[1;32;40m*********************************\033[m")
print("\033[1;31;40m***** FUNDAMENTOS DE PYTHON *****\033[m")
print("\033[1;32;40m*********************************\033[m\n")

num1 = int(input("Digite um número inteiro: "))

if num1 == 0:
    print(f"Desculpe, mas ZERO não é um número inteiro. \n")
elif num1 % 2 == 0:
    print(f"O número {num1} é par. \n")
else:
    print(f"O número {num1} é ímpar. \n")
    

print("\033[1;32;40m*********************************\033[m")
print("\033[1;31;40m***** FUNDAMENTOS DE PYTHON *****\033[m")
print("\033[1;32;40m*********************************\033[m\n")

num1 = float(input("Digite um número: "))


if num1 == 0:
    print(f"Esse número é nulo. \n")
elif num1 > 0:
    print(f"O número {num1} é positivo.\n")
else:
    print(f"O número {num1} é negativo.\n")
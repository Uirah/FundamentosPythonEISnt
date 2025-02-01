
print("\033[1;32;40m*********************************\033[m")
print("\033[1;31;40m***** FUNDAMENTOS DE PYTHON *****\033[m")
print("\033[1;32;40m*********************************\033[m\n")

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
num3 = float(input("Digite mais um número: "))


if num1 >= num2 and num1 >= num3:
    print(f"O número {num1} é o maior dentre esses números.\n")
elif num2 >= num1 and num2 >= num3:
    print(f"O número {num2} é o maior dentre esses números.\n")
else:
    print(f"O número {num3} é o maior dentre esses números.\n")
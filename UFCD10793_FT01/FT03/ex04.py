
print("\033[1;32;40m*********************************\033[m")
print("\033[1;31;40m***** FUNDAMENTOS DE PYTHON *****\033[m")
print("\033[1;32;40m*********************************\033[m\n")

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))

if num1 == num2:
    print(f"Esses número são iguais. \n")
elif num1 > num2:
    print(f"{num1} é maior do que {num2} \n")
else:
    print(f"{num2} é maior do que {num1} \n")
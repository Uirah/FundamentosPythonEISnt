# Importar o módulo cabecalho
from modulos import cabecalho


# Exibir o cabeçalho
cabecalho.exibir_cabecalho()

num1 = int(input("Introduza um número limite\n---> "))
num2 = int(input("Introduza o outro número limite\n---> "))

if num1 < num2:
    for numero in range (num1, num2+1):
        print(f"{numero}")
elif num1 > num2:
    for numero in range (num2, num1+1):
        print(f"{numero}")
else:
    print(f"Os números precisam ser diferentes.")
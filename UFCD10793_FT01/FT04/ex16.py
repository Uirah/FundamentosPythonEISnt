# Importar o módulo cabecalho
from modulos import cabecalho


# Exibir o cabeçalho
cabecalho.exibir_cabecalho()

num = float(input("Introduza um número entre 0 e 10\n---> "))

while not 0 >= num and not num >= 10:
    print("Parabéns, o número está dentro desse intervalo. :)\n")
    num = float(input("Introduza outro número entre 0 e 10\n---> "))

print("Desculpa, mas esse número está fora do intervalo pedido.\nGAME OVER :(\n")
      
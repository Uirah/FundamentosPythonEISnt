# Importar o módulo cabecalho
from modulos import cabecalho


# Exibir o cabeçalho
cabecalho.exibir_cabecalho()

lista = [5,5,5]

mult = int(input("Escolha o valor a multiplicar a lista: "))

for num in lista:
    mult *= num

print(f"Resultado: {mult}")
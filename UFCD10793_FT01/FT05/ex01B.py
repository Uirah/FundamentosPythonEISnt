# Importar o módulo cabecalho
from modulos import cabecalho


# Exibir o cabeçalho
cabecalho.exibir_cabecalho()

for valor in range (1,11):
    for numero in range(1,11):
        print(f"{valor} x {numero} = {valor*numero}")
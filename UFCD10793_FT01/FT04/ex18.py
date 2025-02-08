# Importar o módulo cabecalho
from modulos import cabecalho


# Exibir o cabeçalho
cabecalho.exibir_cabecalho()

print("Pares entre 1 e 200: ")
for count in range (1,201):
    if count %2 == 0:
        print(f"{count}")
    else:
        continue

print()
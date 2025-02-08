# Importar o módulo cabecalho
from modulos import cabecalho


# Exibir o cabeçalho
cabecalho.exibir_cabecalho()

count=0
print("***** A Tabuada de 5 *****")
while count <= 10:
    print(f"{count} x 5 = {count*5}")
    count+=1
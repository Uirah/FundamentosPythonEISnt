# Importar o módulo cabecalho
from modulos import cabecalho


# Exibir o cabeçalho
cabecalho.exibir_cabecalho()

num = int(input("De qual número queres ver a tabuada?\n---> "))

count=0
print(f"\n***** A Tabuada de {num} *****\n")
while count <= 10:
    print(f"{count} \tx {num}  \t= {count*num}")
    count+=1
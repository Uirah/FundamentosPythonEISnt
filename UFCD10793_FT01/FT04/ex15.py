# Importar o módulo cabecalho
from modulos import cabecalho


# Exibir o cabeçalho
cabecalho.exibir_cabecalho()

num = int(input("Introduza um número a ser mostrado seus primeiros 20 múltiplos\n---> "))

for i in range (1, 21):
        print(f"{i*num}")
        i+=1

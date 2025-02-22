# Importar o módulo cabecalho
from modulos import cabecalho

# Exibir o cabeçalho
cabecalho.exibir_cabecalho()

cores=["amarelo", "azul", "branco", "preto", "verde"]

#a
for i in cores:
    print(i)
print()

#b
print(cores[2])

#c
cores[0] = "vermelho"

#d
for i in cores:
    print(i)
print()

#e
cores.append("amarelo")
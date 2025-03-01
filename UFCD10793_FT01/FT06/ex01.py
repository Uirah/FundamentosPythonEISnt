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
print()

#c
cores[0] = "vermelho"

#d
for i in cores:
    print(i)
print()

#e
cores.append("amarelo")

#f
for i in cores:
    print(i)
print()

#g
cores.insert(2, "roxo")

#h
for i in cores:
    print(i)
print()

#i
cores.pop(-1)

#j
for i in cores:
    print(i)
print()

#k
print(len(cores))
print()
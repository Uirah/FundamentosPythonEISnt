# Importar o módulo cabecalho
from modulos import cabecalho
from random import random
from statistics import mean, stdev

# Exibir o cabeçalho
cabecalho.exibir_cabecalho()

lista = []

for nume in range(1, 101):
    lista.append(random())
    
print(f"Maior número: {max(lista)}")
print(f"Menor número: {min(lista)}")
print(f"Soma dos números: {sum(lista)}")
print(f"A média dos números gerados: {mean(lista)}")
print(f"O desvio padrão dos números gerados: {stdev(lista)}\n")

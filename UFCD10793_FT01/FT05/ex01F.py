# Importar o módulo cabecalho
from modulos import cabecalho


# Exibir o cabeçalho
cabecalho.exibir_cabecalho()

'''Escreve um programa, em python, que verifique se uma lista é vazia ou não.
Caso a lista seja vazia, mostre True, caso contrário False.
'''

lista = [1,2,3]
contagem = len(lista)
#print(contagem)

if contagem == 0:
    print("Lista vazia.\n")
    
else:
    print("A lista não está vazia.\n")
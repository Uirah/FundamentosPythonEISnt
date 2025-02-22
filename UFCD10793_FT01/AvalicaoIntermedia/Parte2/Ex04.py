'''Modificar o programa anterior para acrescentar mais uma linha ao ficheiro.'''
import os

try:
    with open("novo_ficheiro.txt", "a") as ficheiro:
        ficheiro.write("Linha adicional do Exer 04\n")
        
    with open("novo_ficheiro.txt", "r") as ficheiro:
        conteudo = ficheiro.read()
        print(f"\nO ficheiro agora está assim: \n\n{conteudo}\n")
        
    

except Exception as e:
    print("Erro inesperado:", e)
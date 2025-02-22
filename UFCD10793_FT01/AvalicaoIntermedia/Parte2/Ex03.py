'''Criar um programa que escreva três linhas num ficheiro novo.'''
import os

try:
    with open("novo_ficheiro.txt", "w") as ficheiro:
        ficheiro.write("Linha 1 nova\n")
        ficheiro.write("Linha 2 nova\n")
        ficheiro.write("Linha 3 nova\n")
        
    with open("novo_ficheiro.txt", "r") as ficheiro:
        conteudo = ficheiro.read()
        print(f"\nO ficheiro selecionado agora está assim: \n\n{conteudo}\n")

except Exception as e:
    print("Erro inesperado:", e)
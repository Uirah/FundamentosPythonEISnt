'''Criar um programa que leia um ficheiro de texto e exibir o seu conteúdo'''
import os

while True:
    try:
        caminho = input("Digite o caminho do ficheiro: ")

        if os.path.exists(caminho):
            with open(caminho, "r") as ficheiro:
                print(f"\nO ficheiro selecionado contém: \n\n{ficheiro.read()}\n")
                break
        else:
            print("Erro: O ficheiro não foi encontrado.")
    except Exception as e:
        print("Erro inesperado:", e)
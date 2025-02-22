'''Modificar o exercício anterior para exibir o conteúdo linha por linha.'''
import os

while True:
    try:
        caminho = input("Digite o caminho do ficheiro: ")

        if os.path.exists(caminho):
            with open(caminho, "r") as ficheiro:
                for linha in ficheiro:
                    print(linha.strip())
            break
            
        else:
            print("Erro: O ficheiro não foi encontrado.")
    except Exception as e:
        print("Erro inesperado:", e)
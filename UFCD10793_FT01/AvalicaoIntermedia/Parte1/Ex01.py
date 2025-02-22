'''Escreva um programa que pede ao utilizador um número inteiro e trata
erros de entrada.'''


while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        print(f"Número inserido: {numero}\n")
        break
    except ValueError:
        print("Erro: O valor deve ser um número inteiro.\n")
        
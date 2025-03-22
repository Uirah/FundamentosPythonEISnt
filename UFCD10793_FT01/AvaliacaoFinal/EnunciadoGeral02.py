"""Escreve uma função em Python que dada uma palavra retorne o número de vogais nessa
palavra."""

def contagem_vogais(palavra):
    contagem = 0
    for vogal in palavra:
        if vogal in "aeiou":
            contagem +=1
    return print(f"\nEssa palavra tem {contagem} vogais.\n")

def main():
    lista = []

   
    print("\n\033[1;31;47m***** Contagem de Vogais *****\033[m\n")

    palavra = input("Qual a palavra a ser testada: ")
    
    contagem_vogais(palavra)
        

# Executar o programa
if __name__ == "__main__":
    main()
"""Escreve uma função em Python que dada uma lista de números imprime a soma
dos valores dessa lista, o número de elementos da lista e a media desses
valores."""

def funcoes(listinha):
    soma = 0
    count = 0
    for nume in listinha:
        soma += nume
        count += 1
    print(f"A soma desses elementos é = {soma}\n")
    media = soma/count
    return print(f"A média desses elementos é = {round(media, 3)}\n")


listinha = [1,5,6,4,6,899,6,4,6,8,4,7]
funcoes(listinha)
        
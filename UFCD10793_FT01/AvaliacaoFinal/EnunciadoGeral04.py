"""Utilizando a biblioteca NumPy :
a. Cria um array de números 1 com shape (8, 2)
b. Cria um array de zeros com shape (5, 7)
c. Subtraia o novo array de outro com dados aleatórios e armazene o numa variável
chamada subarray
d. Calcula a média dos valores do array subarray"""

import numpy as np

#a
uns = np.ones((8, 2))
print(uns)

#b
zerositos = np.zeros((5, 7))
print(zerositos)

#c
array_aleatorio = 0 + 10 *np.random.random((5, 7))
#print(array_aleatorio)
subarray = array_aleatorio - zerositos
print(subarray)

#d
media_array = np.mean(subarray)
print(media_array)
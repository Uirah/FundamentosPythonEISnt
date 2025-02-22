'''Elabora uma script em python que peça ao utilizador um número e some todos
os números de 1 até esse mesmo número. Deves utilizar o tratamento de
erros'''

lista_num = []

num_final = int(input("Digite um número: "))

for numero in range (num_final):
    lista_num.append(numero)
    
print(lista_num)
contagem = 0
if 1 in lista_num:
    contagem+=1
    
print(contagem)
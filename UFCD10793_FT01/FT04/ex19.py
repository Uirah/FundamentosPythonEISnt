# Importar o módulo cabecalho
from modulos import cabecalho


# Exibir o cabeçalho
cabecalho.exibir_cabecalho()

num = int(input("Digite um número inteiro\n--->"))
count = 1
todos_lista = []

for count in range(1,num+1):
    
    todos_lista.append(count)
    count+=1


#print(todos_lista)
reve = list(reversed(todos_lista))
#print(reve)

i=1   
print()
for i in range (1, num+1):
    print(f"{todos_lista[i-1]}\t\t{reve[i-1]}")
    i+=1
# Importar o módulo cabecalho
from modulos import cabecalho


# Exibir o cabeçalho
cabecalho.exibir_cabecalho()

num = int(input("Queres o fatorial de qual número? \n---> "))

if num < 0:
    print("Esse número deve ser um número natural (inteiro positivo).")
    

fatorial = 1
for i in range(1, num + 1):
    
    fatorial *= i
    
    
print(f"O fatorial do número {num} é: {fatorial}")
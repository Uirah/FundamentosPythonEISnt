# Importar o módulo cabecalho
from modulos import cabecalho


# Exibir o cabeçalho
cabecalho.exibir_cabecalho()

nums = int(input("Quantos números queres somar? \n---> "))

count = 0
soma_total = 0

while count <= nums:
    
    soma_total  += count
    count+=1
    
print(f"A soma total é {soma_total}")
    
    
# Importar o módulo cabecalho
from modulos import cabecalho


# Exibir o cabeçalho
cabecalho.exibir_cabecalho()

nums = int(input("Qual o teu número N ? \n---> "))


soma_total = 0
produto_total = 1
count1 = 0
while count1 <= nums:
    
    soma_total  += count1
    count1+=1

count2 = 1
while count2 <= nums:
    
    produto_total *= count2
    count2+=1
    
    
    
print(f"A soma dos primeiros {nums} números é : {soma_total}")
print(f"O produto dos primeiros {nums} números é : {produto_total}")
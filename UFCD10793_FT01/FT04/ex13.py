# Importar o módulo cabecalho
from modulos import cabecalho


# Exibir o cabeçalho
cabecalho.exibir_cabecalho()

soma = 0

for numero in range (10, 101):
    soma += numero
    
print(f"A soma entre 10 e 100 é {soma}")
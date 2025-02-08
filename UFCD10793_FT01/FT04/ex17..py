# Importar o módulo cabecalho
from modulos import cabecalho


# Exibir o cabeçalho
cabecalho.exibir_cabecalho()


num_total = 0
count=1
for count in range (1,21):
    if count == 20:
        nums = float(input(f"Digite mais {21-count} número real\n--->"))
        num_total+=nums
    else:
        nums = float(input(f"Digite {21-count} números reais\n--->"))
        num_total+=nums
    
print(f"\nA soma desses números é: {num_total}\nA média entre eles é: {num_total/20}\n")
    
"""Leia uma cadeia de caracteres no formato “DD/MM/AAAA” e copie o dia, mês e ano para
três variáveis inteiras.
"""


dates = [
    "01/01/2020",
    "15/03/2022",
    "22/05/2023",
    "10/07/2024",
    "31/12/2025"
]
dias = []
meses = []
anos = []
for dia in dates:
    dias.append(int(dia[:2]))
    meses.append(int(dia[3:5]))
    anos.append(int(dia[6:]))
    

#print(dias)
#print(meses)
#print(anos)

print("\n\033[1;31;40mDia\tMês\tAno\033[m")

for show in range(len(dates)):
    print(f"{dias[show]}\t{meses[show]}\t{anos[show]}")
    
print()
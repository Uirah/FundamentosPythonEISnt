#a

datas="12ago2021,02set2020,20jan2022,11out2019,09mar2020,10dez2022"


tudo_junto = ""
cada_data = datas.split(",")
for datinha in cada_data:
    tudo_junto = tudo_junto + "-" + datinha

print(cada_data)
print(tudo_junto)

#b
for datinha in cada_data:
    if "2022" in datinha:
        print(datinha)
        
#c
dias = []

for dia in cada_data:
    dias.append(dia[:2])

print(dias)
    
print(sorted(dias))
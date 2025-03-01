idades=[25, 15, 19, 22, 37, 78, 46, 2, 67]

# a
contagem = 0
for idade in idades:
    if idade < 18:
        contagem += 1
    
print(f"Existem {contagem} pessoas menores de idade\n")

#b
idades_decres = sorted(idades, reverse=True)

print(idades_decres)

#c
idadinha = int(input("Qual idade queres pesquisar?\n"))

if idadinha in idades:
    print("Essa idade está na lista.")
else:
    print("Não existe alguém com essa idade na lista")
    
# [  variável cabeçalho_do_ciclo_onde_se_encontra_a_variavel condição_do_ciclo   ] comprehension lists
menores_idade = [x for x in idades if x<18]
print(len(menores_idade))

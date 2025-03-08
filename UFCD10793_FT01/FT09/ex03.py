#a. Instancie o seguinte dicionário:
computadores_1={
 "Marca":"Asus",
 "Ecra":"14Pol",
 "RAM": [4, 8, 12]
  }
#b. Acrescente um novo elemento à lista com chave igual a “Disco” e valor [“128G”, “256G”]
computadores_1.update({"Disco":["128G", "256G"]})

#c. Permita ao utilizador introduzir um valor específico de RAM e verificar se esta está presente na lista.
ram_pesquisa = int(input("Qual o valor de RAM que pretendes? "))
if ram_pesquisa in computadores_1["RAM"]:
    print("Esse tipo de RAM está presente em nossos dados  :)\n")
else:
    print("Não existe esse tipo de RAM.")
   
#d. Acrecente 16 como novo valor de RAM.
computadores_1["RAM"].append(16)
print(computadores_1)

#e. Copie o dicionário para um novo usando Deep Copy().
computadores_2 = computadores_1.copy()

#f. Na lista nova modifique a marca para “Lenovo” e os valores da RAM para [4,8]. Imprima a nova lista
computadores_2["Marca"] = "Lenovo"
computadores_2["RAM"] = [4,8]
#print(computadores_1)
print(computadores_2)

#g. Crie uma nova lista com deep copy e modifique a marca para “HP” e Disco para [“256G”]- Imprima a respetiva lista
computadores_3 = computadores_1.copy()
computadores_3["Marca"] = "HP"
computadores_3["Disco"] = ["256G"]
print(computadores_3)

#h. Cria uma lista cujos elementos são os três dicionários.
computadores_todos = [computadores_1, computadores_2, computadores_3]

# i. Imprima as marcas com 128G de RAM
for computador in computadores_todos:
    if "Disco" in computador and "128G" in computador["Disco"]:
        marca = computador["Marca"]
        print(f"A {marca} possui 128G de Disco." )
        
# j. Imprima as marcas com 8 e 12 de RAM
for computador in computadores_todos:
    if "RAM" in computador and 8 in computador["RAM"] and 12 in computador["RAM"]:
        marca = computador["Marca"]
        print(f"A Marca {marca} possui 8 e 12 de RAM." )


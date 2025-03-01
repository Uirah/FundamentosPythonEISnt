nums=[10, 2.5, 7, 11, 7.9, "Python", True,6, 5.8 , "Listas"]

#a 
inteiros = 0
floaters = 0
stringys = 0
boleanos = 0
for item in nums:
    if type(item)== int:
        inteiros+=1
    elif type(item)== float:
        floaters+=1
    elif type(item)== str:
        stringys+=1
    elif type(item)== bool:
        boleanos+=1
        
        
print(f"Existem na lista:\n\t{inteiros} Números inteiros\n\t{floaters} Floats\n\t{stringys} Strings\n\t{boleanos} Boleanos na lista.")


#b
somatoria = 0
for item in nums:
    if type(item)== int:
        somatoria+=item

media = somatoria/inteiros
print(f"A média dos números inteiros é {media}")


#c
lista_int = []
for item in nums:
    if type(item)== int:
        lista_int.append(item)
print(f"A lista só de números inteiros é {lista_int}")



#Com o uso de ListComprehention
# Lista inicial
nums = [10, 2.5, 7, 11, 7.9, "Python", True, 6, 5.8, "Listas"]
# a. Conta a quantidade de cada tipo de dado
inteiros = len([x for x in nums if isinstance(x, int) and not isinstance(x, bool)])

floats = sum(1 for x in nums if isinstance(x, float))
strings = sum(1 for x in nums if isinstance(x, str))
booleanos = sum(1 for x in nums if isinstance(x, bool))
print(f"Inteiros: {inteiros}, Floats: {floats}, Strings: {strings}, Booleanos: {booleanos}")
# b. Calcula a média dos inteiros
valores_inteiros = [x for x in nums if isinstance(x, int) and not isinstance(x, bool)]
media = sum(valores_inteiros) / len(valores_inteiros)
print(media)
# c. Cria uma nova lista só com os inteiros
lista_inteiros = [x for x in nums if isinstance(x, int) and not isinstance(x, bool)]
print(lista_inteiros)
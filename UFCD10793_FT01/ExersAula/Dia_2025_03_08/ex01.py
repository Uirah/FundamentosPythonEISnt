import statistics
nums = input("Introduza números com espaços entre eles: ")

separados = nums.split()
print(separados)

so_nums=[]
for item in separados:
    so_nums.append(int(item))
    
print(so_nums)

media = statistics.mean(so_nums)
print(media)


'''numeros=[int(i) for i in input("Introduza uma sequencia de 10 numeros separados por espaço").split()]
print(f"A média dos números introduzidos é {sum(numeros)/len(numeros)}")'''


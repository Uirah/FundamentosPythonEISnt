txt = """Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos,
funcional, de tipagem dinâmica e forte."""

#a
txt_maiu = txt.upper()
print(txt_maiu)

#b
palavra = input("Qual a palavra queres verificar no texto? \n")

if palavra.upper().strip() in txt_maiu:
    print(f"A palavra '{palavra.strip()}' está presente no texto.  :)\n")
    
else:
    print(f"A palavra '{palavra.strip()}' não foi encontrada no texto.  :(\n")
    


#c
count = 0

for x in txt_maiu:
    if "O" in x:
        count = count +1

print(f"A letra 'O' aparece {count} vezes no texto.")

#d
txt=txt.replace("P", "_")
       

print(txt)
        
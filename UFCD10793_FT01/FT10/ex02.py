prov = """o pior cego é aquele que não quer ver."""

prov = prov.capitalize()
print(prov)

palavras = prov.split(" ")
print(palavras)

count = 0

for x in palavras:
    if "que" in x:
        count = count +1
        
print(count)


prov = prov.replace("quer ver", "compra um cão")
print(prov)
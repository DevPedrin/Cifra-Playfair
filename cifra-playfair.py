# Trabalho Cifra Playfair - Pedro Henrque Pereira

alfabeto = list("ABCDEFGHIJLMNOPQRSTUVWXYZ")
word = 'ATACAR'
word = "".join(dict.fromkeys(word))

for char in word:
    indice = alfabeto.index(char)
    alfabeto.pop(indice)

res = ''.join(list(word) + alfabeto)
matriz = [list(res[i*5:(i+1)*5]) for i in range(5)]

#print(matriz)
for linha in matriz:
    print(linha)
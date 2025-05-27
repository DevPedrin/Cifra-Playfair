# Trabalho Cifra Playfair - Pedro Henrque Pereira

alfabeto = list("ABCDEFGHIJLMNOPQRSTUVWXYZ")
chave = input("Digite a chave: ")


def preparar_chave(chave):
    chave = chave.upper() 
    chave = "".join(dict.fromkeys(chave)) # Remove letras repetidas
    return chave

chave = preparar_chave(chave)
print(chave)

def matriz(chave):
    for char in chave:
        indice = alfabeto.index(char)
        alfabeto.pop(indice) # remove as letras que ja tem na chave

    res = ''.join(list(chave) + alfabeto)
    matriz = [list(res[i*5:(i+1)*5]) for i in range(5)]
    return matriz

matriz = matriz(chave)

def preparar_texto(texto):
    pass

def criptografar(chave, texto):
    pass




#print(matriz)
for linha in matriz:
    print(linha)
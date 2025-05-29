# Trabalho Cifra Playfair - Pedro Henrique Pereira

import numpy as np

alfabeto = list("ABCDEFGHIJLMNOPQRSTUVWXYZ")

chave = input("Digite a chave: ")
texto = input("Digite o texto claro: ")

def preparar_chave(chave):
    chave = chave.upper().replace("K", "X")
    chave = "".join(dict.fromkeys(chave)) 
    return chave

chave = preparar_chave(chave)

def montar_matriz(chave):
    for letra in chave:
        if letra in alfabeto:
            alfabeto.remove(letra)

    res = list(chave + ''.join(alfabeto))
    matriz = np.array(res).reshape(5, 5)
    return matriz

matriz = montar_matriz(chave)

def preparar_texto(texto):
    texto = texto.upper().replace("K", "X")
    texto = ''.join(filter(str.isalpha, texto))
    resultado = []
    i = 0

    while i < len(texto):
        l1 = texto[i]
        if i + 1 < len(texto):
            l2 = texto[i + 1]
            if l1 == l2:
                resultado.append(l1 + 'X')
                i += 1
            else:
                resultado.append(l1 + l2)
                i += 2
        else:
            resultado.append(l1 + 'X')
            i += 1

    return resultado

def encontrar_posicao(matriz, letra):
    pos = np.where(matriz == letra)
    return pos[0][0], pos[1][0]

def criptografar(matriz, texto):
    bigramas = preparar_texto(texto)
    resultado = ""

    for par in bigramas:
        l1, l2 = par[0], par[1]
        r1, c1 = encontrar_posicao(matriz, l1)
        r2, c2 = encontrar_posicao(matriz, l2)

        if r1 == r2:
            resultado += matriz[r1][(c1 + 1) % 5]
            resultado += matriz[r2][(c2 + 1) % 5]
        elif c1 == c2:
            resultado += matriz[(r1 + 1) % 5][c1]
            resultado += matriz[(r2 + 1) % 5][c2]
        else:
            resultado += matriz[r1][c2]
            resultado += matriz[r2][c1]

    return resultado

def decifrar(matriz, texto_cifrado):
    resultado = ""
    i = 0

    while i < len(texto_cifrado):
        l1, l2 = texto_cifrado[i], texto_cifrado[i + 1]
        r1, c1 = encontrar_posicao(matriz, l1)
        r2, c2 = encontrar_posicao(matriz, l2)

        if r1 == r2:
            resultado += matriz[r1][(c1 - 1) % 5]
            resultado += matriz[r2][(c2 - 1) % 5]
        elif c1 == c2:
            resultado += matriz[(r1 - 1) % 5][c1]
            resultado += matriz[(r2 - 1) % 5][c2]
        else:
            resultado += matriz[r1][c2]
            resultado += matriz[r2][c1]

        i += 2

    return resultado

# Exibição da matriz
print("\nMatriz 5x5 gerada:")
for linha in matriz:
    print(linha)

# Execução
texto_cifrado = criptografar(matriz, texto)
print("\nTexto cifrado:", texto_cifrado)

texto_decifrado = decifrar(matriz, texto_cifrado)
print("Texto decifrado (bruto):", texto_decifrado)

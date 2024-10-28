#--------------------------------------------------------------------------
# Programa Questao Exemplo
# Funcoes: fEAM(matrizF, matrizG)
# soma_matriz(matriz)
# cria_matriz_aleatoria(n)
#--------------------------------------------------------------------------

import random
import os

#--------------------------------------------------------------------------
# Funcao fEAM(matrizF, matrizG)
#--------------------------------------------------------------------------
def fEAM(matrizF, matrizG) :
    EMA = 0
    linhas = len(matrizF)
    colunas = len(matrizF[0])

    for i in range(linhas):
        for j in range(colunas):
            dif = + abs(matrizF[i][j]-matrizG[i][j])

    EMA = dif/(linhas*colunas)
    return EMA

#--------------------------------------------------------------------------
# Funcao soma_matriz(matriz)
#--------------------------------------------------------------------------
def soma_matriz(matriz) :
    soma = 0
    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        for j in range(colunas):
            soma = soma + matriz[i][j]

    return soma

#------------------------------------------------------------------------------
# Funcao cria_matriz_aleatoria(n)
#------------------------------------------------------------------------------
def cria_matriz_aleatoria(n) :
    lista = []

    for y in range(n):
        linha = []

    for x in range(n):
        den = random.randint(1,10);
        num = random.randint(1,100)/den
        linha.append(num)
        lista.append(linha)

    return lista
#------------------------------------------------------------------------------
# Funcao main()
#------------------------------------------------------------------------------
def main() :

    n = int(input("Digite a dimensao da matriz: "))
    matrizF = cria_matriz_aleatoria(n)
    matrizG = cria_matriz_aleatoria(n)
    print(matrizF)
    print(matrizG)

    EMA = fEAM(matrizF, matrizG)
    print("Erro Medio Absoluto: " + str(EMA))

    #soma = soma_matriz(matriz)
    #print(’Soma acumulada de todos os elementos da matriz: ’ + str(soma))

    return
    
#------------------------------------------------------------------------------
# Programa Principal
#------------------------------------------------------------------------------
main()
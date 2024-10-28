print("Aluno: Eduardo Santos Ferreira")

#Questão 3 - [ 2.50 ponto(s) ] - Escreva uma função que calcule a distância 𝐷 entre dois pontos
# de um plano, sendo fornecidas as coordenadas X1, Y1 e X2, Y2.

#Declarando função
def distancia(X1, Y1, X2, Y2):
    D = ((X2 - X1) ** 2 + (Y2 - Y1) ** 2) ** 1/2
    return D

#Recebendo dados do usuário
X1 = float(input("X1: "))
Y1 = float(input("Y1: "))
X2 = float(input("X2: "))
Y2 = float(input("Y2: "))

#Retornando resultado
print(distancia(X1, Y1, X2, Y2))
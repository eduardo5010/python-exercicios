print("Aluno: Eduardo Santos Ferreira")

#Importando biblioteca
import math

#Questão 2 - Escreva duas funções que recebam o raio r de uma esfera. A primeira calculará e 
# retornará o volume da esfera (4/3 π r3)
# e a segunda, retornará a área da superfície da esfera (4 πr2). 
#Escreva também um programa principal que use estas funções, a partir de n raios digitados.

#Definindo funções
def volumeEsfera(r):
    V = (4/3) * math.pi * r ** 2
    return V
def areaSuperficieEsfera(r):
    AS = 4 * math.pi * r ** 2
    return AS

#Início do programa
r = float(input("Digite o raio da esfera em metros: "))
V = volumeEsfera(r)
AS = areaSuperficieEsfera(r)
print("O volume e a área da superfície da esfera são, respectivamente {:.2f} m3 e {:.2f} m2.".format(V, AS))
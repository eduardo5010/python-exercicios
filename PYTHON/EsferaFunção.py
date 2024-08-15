print("Aluno: Eduardo Santos Ferreira")

#Importando biblioteca
import math

#Questão 3 - Escreva uma única função que receba o raio r de uma esfera e retorne os dois valores 
# produzidos pelas duas funções da questão anterior. O primeiro valor será o volume da esfera e o 
# segundo será a área da superfície da esfera. Escreva também um programa principal que use esta 
# função, a partir de vários raios digitados. O programa termina quando encontra um raio negativo 
# ou zero.

#Definindo função
def AreaVolume(r):
    V = (4/3) * math.pi * r ** 2
    AS = 4 * math.pi * r ** 2
    return V, AS

#Definindo programa principal
def main():
    r = float(input("Digite o raio da esfera em metros: "))
    while(r > 0):
        V, AS = AreaVolume(r)
        print("O volume e a área da superfície da esfera são, respectivamente {:.2f} m3 e {:.2f} m2.".format(V, AS))
        r = float(input("Digite o raio da esfera em metros: "))

main()
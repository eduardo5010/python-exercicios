print("Aluno: Eduardo Santos Ferreira")

#Questão 4 - [ 2.50 ponto(s) ] - Escreva uma função que calcule o valor aproximado de 𝑒 para
# 6 termos através da série da equação 2. Construa uma outra função para calcular o fatorial de
# forma recursiva.

#Definindo funções
def fatorial(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n * fatorial(n - 1)

def euler():
    e = 1/fatorial(0) + 1/fatorial(1) + 1/fatorial(2) + 1/fatorial(3) + 1/fatorial(4) + 1/fatorial(5)
    return e

#Retornando resultado
print(euler())
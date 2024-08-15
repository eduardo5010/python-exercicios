print("Aluno: Eduardo Santos Ferreira")

#Faça um programa que receba três números e mostre-os em ordem crescente.

#Solicitando dados ao usuário
N1 = float(input("Digite o primeiro número: "))
N2 = float(input("Digite o segundo número: "))
N3 = float(input("Digite o terceiro número: "))

#Verificado e retornando os números em ordem crescente
if (N1 > N3):
    tmp = N3
    N3 = N1
    N1 = tmp
if (N1 > N2):
    tmp = N2
    N2 = N1
    N1 = tmp
if (N2 > N3):
    tmp = N3
    N3 = N2
    N2 = tmp

#Declarando lista com os números obtidos
numeros = [N1, N2, N3]

#Retornando números
for i in numeros:
    print(i)
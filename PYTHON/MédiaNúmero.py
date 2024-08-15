print("Aluno: Eduardo Santos Ferreira")

#Crie um programa que entre com 𝑛 números (informado pelo usuário) e imprima a média
# desses números.

#Declarando variáveis
soma = 0
numeros = []

#Delimitando condicionais
quantidade = int(input("Digite a quantidade de números a serem inseridos: "))
for i in range(0, quantidade, 1):
    numeros.append(float(input("Digite um número: ")))
    soma += numeros[i]
    if(i == quantidade-1):
        media = soma / quantidade
        #Retornando resultado
        print("A média dos números é {}.".format(media))
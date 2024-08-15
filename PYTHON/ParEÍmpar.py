print("Aluno: Eduardo Santos Ferreira")

#Crie um programa que entre com 20 números e imprima quantos são pares e quantos são
# ímpares.

#Declarando variáveis
par = 0
impar = 0

#Delimitando condicionais
for i in range(0, 20, 1):
    #Recebendo valores
    numero = float(input("Digite um número: "))
    x = numero%2 == 0
    #Computando pares e ímpares
    if(x):
        par += 1
    else:
        impar += 1
#Retornando resultados
print("Dos números inseridos, {} são pares e {} são ímpares.".format(par, impar))
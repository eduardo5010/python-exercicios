print("Aluno: Eduardo Santos Ferreira")

#Crie um programa que imprima todos os números de 1 até 1000. No final o programa deve
# imprimir a soma acumulada de todos os números entre 1 até 1000

#Declarando variáveis
soma = 0

#Delimitando condicionais
for i in range(1, 1001, 1):
    #Imprimindo resultado
    print(i)
    soma += i
    if(i == 1000):
        #Imprimindo soma de todos os resultados
        print(soma)
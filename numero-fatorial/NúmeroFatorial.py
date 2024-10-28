print("Aluno: Eduardo Santos Ferreira")

#Escreva um programa que receba do usuário um número 𝑛 inteiro e escreva na tela o fatorial
# de 𝑛, como no exemplo abaixo. Caso o número 𝑛 tenha algum número menor que zero, o programa deve
# retornar uma mensagem de erro: "erro, o valor deve ser positivo!". Implemente usando o laço for. Não
# utilize biblioteca math.

#Declarando variáveis
fatorial = 1

#Solicitando dados ao usuário
numero = int(input("Digite um número: "))

#Delimitando condicional
for i in range(numero, 0, -1):
    #Computando fatorial
    fatorial *= i
    #Complementando casos fora do programa
if(numero <= 0):
    print("Erro, o valor deve ser positivo!")
    #Encerrando programa em caso de número inválido
else:
    #Retornando resultado, caso exista
    print("O fatorial de {} é {}.".format(numero, fatorial))
print("Aluno: Eduardo Santos Ferreira")

#Escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a
# este numero. Isto é, janeiro se 1, fevereiro se 2, e assim por diante. Caso o usuário digite um número
# diferente do solicitado, deve imprimir Erro, mês inválido

#Declarando a função inteiro para mês
def mes_inteiro(mes):
    if mes == 1:
        mes = "Janeiro"
    elif mes == 2:
        mes = "Fevereiro"
    elif mes == 3:
        mes = "Março"
    elif mes == 4:
        mes = "Abril"
    elif mes == 5:
        mes = "Maio"
    elif mes == 6:
        mes = "Junho"
    elif mes == 7:
        mes = "Julho"
    elif mes == 8:
        mes = "Agosto"
    elif mes == 9:
        mes = "Setembro"
    elif mes == 10:
        mes = "Outubro"
    elif mes == 11:
        mes = "Novembro"
    else:
        mes = "Dezembro"
    return mes

#Solicitando dados ao usuário
mes = int(input("Digite o número do mês: "))

#Validando valor recebido
if(mes < 1 or mes > 12):
    print("Erro, mês inválido.")
else:
    #Chamando a função inteiro para mês e retornando o mês por extenso correspondente
    print("O mês equivalente ao número digitado é: {}.".format(mes_inteiro(mes)))
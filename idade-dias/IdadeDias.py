print("Aluno: Eduardo Santos Ferreira")

#Questão 2 - [ 2.50 ponto(s) ] - Faça um programa que leia a idade de uma pessoa expressa em
# anos, meses e dias e mostre-a expressa apenas em dias. Utilize uma função para realizar esse
# cálculo. Para efeito dos cálculos, um mês tem 30 dias. Utilize o padrão apresentado nos exemplos.

#Definindo função
def contarDias(Anos, Meses, Dias):
    dias = Anos*360 + Meses*30 + Dias
    return dias

#Recebendo dados do usuário
Anos = int(input("Anos: "))
Meses = int(input("Meses: "))
Dias = int(input("Dias: "))

#Retornando resultado
print(contarDias(Anos, Meses, Dias))
#Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro).

#Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário fixo: R$ "))
vendas = float(input("Digite o total de vendas no mês: R$ "))
total = salario + vendas * .15
print("O total a receber é R$ {:.2f}".format(total))
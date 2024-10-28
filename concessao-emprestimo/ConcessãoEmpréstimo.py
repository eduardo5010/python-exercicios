print("Aluno: Eduardo Santos Ferreira")

#Faça um programa que leia o salário de um trabalhador e o valor da prestação de um
# empréstimo. Se a prestação for maior que 20% do salário imprima: Empréstimo não concedido,
# caso contrário imprima: Empréstimo concedido.

#Solicitando dados ao usuário
salario = float(input("Digite o valor salário mensal em R$: "))
prestacao = float(input("Digite o valor prestação em R$: "))

#Computando condicionais e retornando valor computado
if(salario * .2 < prestacao):
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")
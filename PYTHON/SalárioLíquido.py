#Faça um programa que receba o salário-base de um funcionário. 

#O programa deve calcular e imprimir o salário a receber, 
# sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base.

#Além disso, o programa deve imprimir o valor do imposto de renda que será de 7% de imposto sobre o salário-base.

salario_base = float(input("Digite o valor do salário-base em R$: "))
gratificacao = salario_base * .05
imposto_de_renda = salario_base * .07
salario_a_receber = salario_base + gratificacao - imposto_de_renda
print("O valor do salário a receber é R$ {:.2f}".format(salario_a_receber))
print("O valor do imposto de renda é R$ {:.2f}".format(imposto_de_renda))
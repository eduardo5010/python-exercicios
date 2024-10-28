#Leia o salário de um funcionário. 

#Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%.

salario = float(input("Digite o valor do salário em R$: "))
aumento = salario * 1.25
print("O valor do salário com aumento é R$ {:.2f}".format(aumento))
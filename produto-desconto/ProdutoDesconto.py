#Faça um programa que leia o valor de um produto e imprima o valor com desconto, 
# tendo em vista que o desconto foi de 12%.

valor = float(input("Digite o valor do produto em R$: "))
desconto = valor - (valor * .12)
print("O valor do produto com desconto é R$ {:.2f}".format(desconto))
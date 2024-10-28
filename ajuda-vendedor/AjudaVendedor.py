#Escreva um programa de ajuda para vendedores.

#A partir de um valor total de uma venda, o programa deve imprimir na tela:

#O total a pagar com desconto de 10%

#O valor de cada parcela, no parcelamento de 3X sem juros;

#A comissão do vendedor de 5% sobre o valor total a pagar com desconto.

valor = float(input("Digite o valor da venda em R$: "))
desconto = valor * 0.9
parcelamento = valor / 3
comissao = desconto * 0.05
print("O valor total a pagar é R$ {:.2f}".format(desconto))
print("O valor das parcelas em 3x sem juros é R$ {:.2f}".format(parcelamento))
print("A comissão a receber é R$ {:.2f}".format(comissao))
print("Aluno: Eduardo Santos Ferreira")

#Escreva um programa (usando FOR) que entre com cinco números e imprima o quadrado
# de cada número.

for i in range(0, 5, 1):
    numero = float(input("Digite o número: "))
    quadrado = numero ** float(2)
    print("O quadrado de {} é {}.".format(numero, quadrado))
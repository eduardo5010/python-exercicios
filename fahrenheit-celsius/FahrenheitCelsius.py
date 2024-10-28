#Faça um programa que leia uma temperatura em graus Fahrenheit e
# apresente-a convertida em graus Celsius.

#A fórmula de conversão é: C = (F − 32) / 1.8, sendo C a temperatura em Celsius
# e F a temperatura em Fahrenheit.

F = float(input("Digite a temperatura em graus Fahrenheit: "))
C = (F - 32) / 1.8
print("A temperatura de {} graus Fahrenheit equivale a {:.1f} graus Celsius.".format(F, C))
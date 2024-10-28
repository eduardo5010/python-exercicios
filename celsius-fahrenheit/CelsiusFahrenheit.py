#Faça um programa que receba uma temperatura em graus Celsius (usando input) e
# apresente-a convertida em graus Fahrenheit.

#A fórmula de conversão é: F = C ∗ (9.0 / 5.0) + 32, sendo F a temperatura em Fahrenheit 
# e C a temperatura em Celsius.

C = float(input("Digite a temperatura em graus Celsius: "))
F = C * (9.0 / 5.0) + 32
print("A temperatura de {} graus Celsius equivale a {:.1f} graus Fahrenheit.".format(C, F))
#Faça um programa que leia uma temperatura em graus Kelvin e
# apresente-a convertida em graus Celsius. 

#A fórmula de conversão é C = K − 273.15, sendo C a temperatura em Celsius 
# e K a temperatura em Kelvin.

K = float(input("Digite a temperatura em graus Kelvin: "))
C = K - 273.15
print("A temperatura de {} graus Kelvin equivale a {:.1f} graus Celsius.".format(K, C))
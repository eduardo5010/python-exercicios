#Eduardo Santos Ferreira

#Importando biblioteca math
import math

#Declarando constantes
g = 9.8

#Solicitando dados ao usuário
v = float(input("Digite a velocidade do arremesso em metros por segundo: "))
a = float(input("Informe o ângulo do arremesso em graus em relação à superfície: "))

#Calculando altura do arremesso
h = ((v ** 2) * (math.sin(a) ** 2)) / (2 * g)

#Retornando valor computado
print("A altura do arremesso é de {:.1f} metros".format(h))
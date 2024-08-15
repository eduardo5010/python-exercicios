#Eduardo Santos Ferreira

#Importando biblioteca math
import math

#Declarando constantes
L = 0.2
C = 2 * (10 ** -6)

#Solicitando dados ao usuário
R1 = float(input("Informe a resistência elétrica da primeira resistência: "))
R2 = float(input("Informe a resistência elétrica da segunda resistência: "))

#Calculando altura do arremesso
f = ((1 / 2) * math.pi) * math.sqrt((L * C * (R1 ** 2 * C * L)/(R2 ** 2 * C * L)))

#Retornando valor computado
print("A frequência de ressonância do circuito do RLC é de {:.1f} hertz".format(f))
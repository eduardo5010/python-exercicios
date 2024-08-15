#Eduardo Santos Ferreira

#Importar biblioteca math
import math

#Declarando constantes
k = 401
pi = math.pi

#Solicitando dados ao usuário
L = float(input("Informe o comprimento do tubo em metros: "))
r1 = float(input("Informe o raio interno do tubo em metros: "))
r2 = float(input("Informe o raio externo do tubo em metros: "))
T1 = float(input("Informe a área da superfície interna do tubo em metros quadrados: "))
T2 = float(input("Informe a área da superfície externa do tubo em metros quadrados: "))

#Calculando taxa de transferência de calor
q = (2 * pi * L * k * (T1 - T2)) / (math.log((r1 / r2)))

#Retornando valor computado
print("A taxa de transferência de calor do tubo é de {:.1f} watts por Celsius metros".format(q))
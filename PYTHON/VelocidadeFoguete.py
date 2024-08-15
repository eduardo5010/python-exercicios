print("Aluno: Eduardo Santos Ferreira")

#A velocidade de um foguete pode ser descrita como:
#𝑣(𝑡) = {
# 10 * t ** 2 - 5 * t, quando 0 <= t < 8
# 624 - 3 * t, quando 8 <= t < 16
# 36 * t + 12(t - 16) ** 2, quando 16 <= t < 26
# 2136𝑒 ** (-.1(t - 26)), quando t > 26
# 0, caso contrário
# }

#Desenvolva um programa em Python para calcular 𝑣 como uma função de 𝑡.

#Importando biblioteca math
import math

#Solicitando valores ao usuário
T = float(input("Digite o valor de T: "))

#Verificando condicionais e computando função correspondente
if(T >= 0 and T < 8):
    I = 10 * T ** 2 - 5 * T
elif(T >= 8 and T < 16):
    I = 624 - 3 * T
elif(T >= 16 and T < 26):
    I = 36 * T + (12 * (T - 16) ** 2)
elif(T > 26):
    I = (2136 * math.e) ** (-.1 * (T - 26))
else:
    I = 0

#Retornando resultado da função
print("A imagem da função da velocidade com o valor informado 𝑣({}) = {}.".format(T, I))
print("Aluno: Eduardo Santos Ferreira")

#Escreva um programa em Python para avaliar uma função 𝑓(𝑥, 𝑦) para quaisquer dois
# valores 𝑥 e 𝑦 especificados pelo usuário. A função 𝑓(𝑥, 𝑦) é definida como:
#𝑓(𝑥, 𝑦) = {
# x + y, quando x >= 0 e y >= 0
# x + y ** 2, quando x >= 0 e y < 0
# x ** 2 + y, quando x < 0 e y >= 0
# x ** 2 + y ** 2, quando x < 0 e y < 0
# }

#Solicitando valores ao usuário
X = float(input("Digite o valor de X: "))
Y = float(input("Digite o valor de Y: "))

#Verificando condicionais e computando função correspondente
if(X >= 0 and Y >=0):
    I = X + Y
elif(X >= 0 and Y < 0):
    I = X + Y ** 2
elif(X < 0 and Y >= 0):
    I = X ** 2 + Y
elif(X < 0 and Y < 0):
    I = X ** 2 + Y ** 2

#Retornando resultado da função
print("A imagem da função com os valores dados é 𝑓({}, {}) = {}.".format(X, Y, I))
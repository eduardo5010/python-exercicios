print("Aluno: Eduardo Santos Ferreira")

#Escreva um programa em Python que leia as coordenadas (𝑥, 𝑦) de um ponto no plano
# e indique em que quadrante [primeiro (+,+), segundo (-,+), terceiro (-,-) ou quarto (+,-)] este ponto se
# encontra. O programa aceita apenas números diferente de 0 (zero). Caso o usuário digite zero o programa
# deve imprimir na tela: erro, X e/ou Y nao pode ser zero

#Solicitando dados ao usuário
X = float(input("Digite o valor do eixo X: "))
Y = float(input("Digite o valor do eixo Y: "))

#Computando condicionais e retornando valor computado
if(Y == 0) or (X == 0):
    print("Erro, X e/ou Y não pode ser zero.")
elif(X > 0):
    if(Y > 0):
        print("As coordenadas informadas pertencem ao primeiro (+,+) quadrante.")
    else:
        print("As coordenadas informadas pertencem ao quarto (+,-) quadarante.")
elif(X < 0):
    if(Y > 0):
        print("As coordenadas informadas pertencem ao segundo (-,+) quadrante.")
    else:
        print("As coordenadas informadas pertencem ao terceiro (-,-) quadrante")
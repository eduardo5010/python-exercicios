print("Aluno: Eduardo Santos Ferreira")

#Questão 5 - Escreva uma função data_por_extenso() que receba uma data no formato 
# DDMMAAAA, num único inteiro e retorne esta data, como um texto, no formato “DD de 
# mês_por_extenso de AAAA”. Use outra função, que será chamada pela primeira função, para 
# converter o mês numérico no mês por extenso. Faça um programa principal para mostrar o 
#funcionamento destas funções, para qualquer data digitada.

#Definindo variável global
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

#Definindo funções
def mes_por_extenso(MM):
    global meses
    for i in range(-1, 12, 1):
        if (int == i+1):
            return meses[i]
def data_por_extenso(DD, MM, AAAA):
    return "{} de {} de {}".format(DD, mes_por_extenso(MM), AAAA)

#Definindo programa principal
def main():
    DDMMAAAA = int(input("Digite a data no formato DDMMAAAA: "))
    DD = str(DDMMAAAA).split(" ")[1]
    print(DD)
    MM = str(DDMMAAAA).split(str(DDMMAAAA)[2])
    print(MM)
    AAAA = str(DDMMAAAA).split(str(DDMMAAAA)[3])
    print(AAAA)
    print(data_por_extenso(DD, MM, AAAA))

main()
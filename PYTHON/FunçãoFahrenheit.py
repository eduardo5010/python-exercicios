print("Aluno: Eduardo Santos Ferreira")

#Questão 4 - Escreva uma função convFahr() que converte uma temperatura em graus Fahrenheit 
# para graus Celsius ou Kelvin. A função recebe como argumentos de entrada uma temperatura em 
# graus Fahrenheit e um caractere (“C” ou “K”), indicando a unidade de temperatura que a função 
# retornará. Se for informado um “C” a temperatura em graus Fahrenheit será convertida para 
# temperatura em graus Celsius e se for informado um “K” será em graus Kelvin. Os fatores de 
# conversão são: C = (F 32) * 5/9 e K = C + 273,15. Escreva um programa principal que use esta 
# função, use um menu para a escolha da conversão de várias temperaturas e tenha uma opção de 
#encerramento do programa

#Definindo função
def convFahr(F, T):
    C = (F - 32) / 1.8
    if(T == "C"):
        return C
    if(T == "K"):
        K = C + 273.15
        return K

#Definindo programa principal
def main():
    T = input("Escolha a unidade de temperatura para que deseja converter: \nC. Graus Celsius\nK. Graus Kelvin\nF. Encerrar programa\nDigite C ou K (ou F): ").upper()
    if(T == "F"):
        return 0
    F = float(input("Digite a temperatura em graus Fahrenheit: "))
    while(T != "F"):
        CK = convFahr(F, T)
        if(T == "C"):
            T = "Celsius"
        if(T == "K"):
            T = "Kelvin"
        print("A temperatura de {:.2f} graus Fahrenheit equivale a {:.2f} graus {}.".format(F, CK, T))
        T = input("Escolha a unidade de temperatura para que deseja converter: \nC. Graus Celsius\nK. Graus Kelvin\nF. Encerrar programa\nDigite C ou K (ou F): ").upper()
        if(T == "F"):
            break
        F = float(input("Digite a temperatura em graus Fahrenheit: "))

main()
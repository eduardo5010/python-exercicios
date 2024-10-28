print("Aluno: Eduardo Santos Ferreira")

#Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se for
# divisível por 400 ou se for divisível por 4 e não for divisível por 100. Por exemplo: 1988, 1992, 1996.

#Solicitando dados ao usuário
ano = int(input("Digite o ano: "))

#Verificando e retornando resultado
if (ano%4 != 0) or (ano%400 != 0):
    print("O ano informado não é bissexto.")
else:
    print("O ano informado é bissexto.")
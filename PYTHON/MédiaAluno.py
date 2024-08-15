print("Aluno: Eduardo Santos Ferreira")

#Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na
# tela a mádia destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde
# caso a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa termina.

#Solicitando dados ao usuário
N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))

#Computando condicionais
if(N1 < 0 or N1 > 10) or (N2 < 0 or N2 > 10):
    print("As notas digitadas são inválidas, valores devem ser entre 0.0 e 10.0.")
else:
    #Calculando a média aritmética e retornando valores computados
    M = (N1 + N2) / 2
    print("A média do aluno é igual a {:.1f}".format(M))
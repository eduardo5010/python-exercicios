print("Aluno: Eduardo Santos Ferreira")

#Solicitar ao usuário 10 valores para serem armazenados em um vetor e
# mostrar todos os elementos fornecidos na ordem inversa de solicitação.

a = []
for i in range (0, 10, 1):
    a.append(input("Digite o elemento: "))
for i in range (9, -1, -1):
    print(a[i])
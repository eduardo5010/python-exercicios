print("ALuno: Eduardo Santos Ferreira")

#Ler as notas de 50 alunos e mostrar a média delas

notas= []

for i in range(0, 50 ,1):
    notas.append(float(input("Digite a nota %d: " % (i + 1))))
print(notas)
media = sum(notas)/len(notas)
print(media)
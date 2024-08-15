print("Aluno: Eduardo Santos Ferreira")

#Definindo função
def r5tot(r1, r2, r3, r4, r5):
    Req = 1/r1 + 1/r2 + 1/r3 + 1/r4 + 1/r5
    return Req

#Início do programa
r1 = float(input("Digite o valor da resistência 1 (Ohm): "))
r2 = float(input("Digite o valor da resistência 2 (Ohm): "))
r3 = float(input("Digite o valor da resistência 3 (Ohm): "))
r4 = float(input("Digite o valor da resistência 4 (Ohm): "))
r5 = float(input("Digite o valor da resistência 5 (Ohm): "))

#Chamando função
Req = r5tot(r1, r2, r3, r4, r5,)
print("A resistência equivalente dos resistores é de {} ohms.".format(Req))
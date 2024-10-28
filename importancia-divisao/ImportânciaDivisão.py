#A importância de R$780.000,00 será dividida entre três ganhadores de um concurso.

#Sendo que da quantia total:

#O primeiro ganhador receberá 46%;

#O segundo receberá 32%;

#O terceiro receberá o restante;

#Calcule e imprima a quantia ganha por cada um dos ganhadores.

print("A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso.")
importancia = 780000 * .46
print("O primeiro ganhador receberá 46%, que equivale a R$ {:.2f}".format(importancia))
importancia = 780000 * .32
print("O segundo receberá 32%, que equivale a R$ {:.2f}".format(importancia))
importancia = 780000 - (780000 * (.46 + .32))
print("O terceiro receberá o restante, equivalendo a R$ {:.2f}".format(importancia))
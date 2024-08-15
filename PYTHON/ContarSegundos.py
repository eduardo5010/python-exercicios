print("Aluno: Eduardo Santos Ferreira")

#Questão 1 - [ 2.50 ponto(s) ] - Escreva um programa que leia a hora, minuto e segundo e dê o
# resultado em segundos. Escreva uma função para fazer os cálculos. Utilize o padrão apresentado
# nos exemplos.

import time

#Definindo função
def contarSegundos(hora, min, seg):
    segundos = hora*3600 + min*60 + seg
    return segundos

def segundosParaHoras(segundos):
    return time.strftime("%H:%M:%S", time.gmtime(segundos)) 

#Recebendo dados do usuário
hora = int(input("hora: "))
min = int(input("min: "))
seg = int(input("seg: "))

#Retornando resultado
print(contarSegundos(hora, min, seg))
print(segundosParaHoras(contarSegundos(hora, min, seg)))
print("Aluno: Eduardo Santos Ferreira")

#Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12, e
# se o dia existe naquele mês. Note que Fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não
# bissexto

#Solicitando dados ao usuário
data = input("Digite uma data no fomato DD/MM/AAAA: ")

#Resgatando números da variável em string para inteiro
data = data.split("/")
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])

#Verificando validade da data informada e retornando resultado
if(mes < 1 or mes > 12):
    print("Erro, data inválida.")
elif((ano%4 != 0) or (ano%400 != 0)) and (dia > 28 and mes == 2):
    print("Erro, data inválida.")
elif(mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
    if(dia > 30):
        print("Erro, a data inválida")
elif(dia < 1 or dia > 31):
    print("Erro, data inválida.")
else:
    print("A data é válida.")
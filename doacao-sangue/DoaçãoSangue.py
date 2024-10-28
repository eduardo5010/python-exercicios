print("Aluno: Eduardo Santos Ferreira")

#Você foi contratado para desenvolver um programa com o objetivo de agilizar a triagem de
# doadores de sangue. Os requisitos para doação são:
#• Ter entre 16 e 69 anos.
#• Pessoas acima de 60 anos só pode doar se já tiverem doado sangue alguma vez antes dessa idade.
#• Pesar no mínimo 60kg se for do sexo masculino e 50kg se for do sexo feminimo.

#Existe alguns requisitos de quem não pode doar sangue:
#• Estiver com febre no dia da doação.
#• Estiver grávida.
#• Estiver amamentando, a menos que o parto tenha ocorrido há mais de 12 meses.

#Crie um programa que receba os dados de entrada e informe se a pessoa pode ou não doar sangue.

#Para perguntas com resposta booleana (sim ou nao), use como entrada valores booleanos. Para a
# pergunta sobre o sexo do doador, use como padrão 𝐹=FEMINIMO e 𝑀=MASCULINO como dados de
# entrada. Observe que dependendo do sexo, algumas perguntas podem mudar. Exemplo: Se o doador
# for do sexo masculino, o programa não deve perguntar se está gravida. Caso por algum motivo não seja
# possível realizar a doação de sangue, o programa deve informar os motivos. Exemplo do funcionamento
# do programa:

#TERMINAL
#   Informe o sexo do doador (digite F para feminino e M para masculino): F
#   Informe a idade: 45
#   Informe o peso: 56
#   A doadora esta gravida (digite sim ou nao)?: sim
#   Nao eh possivel doar sangue
#   A doadora esta gravida!

#Solicitando dados ao usuário e verificando condiconais
sexo = input("Digite o sexo (digite F para feminino e M para masculino): ")
#Solicitando sexo e verificando condicionais
if(sexo == "F" or sexo == "f"):
    #Verificando se está grávida
    gravida = input("Está grávida (S/N): ")
    if(gravida == "N" or gravida == "n"):
        #Verificando se está amamentando
        amamentando = input("Está amamentando (S/N): ")
        if(amamentando == "S" or amamentando == "s"):
            #Verificando tempo desde o parto
            tempo = input("O parto ocorreu há mais de 12 meses (S/N): ")
            if(tempo == "S" or tempo == "s"):
                #Solicitando idade
                idade = int(input("Digite a idade: "))
                #Verificando condicionais de idade
                if(idade < 16 and idade > 69):
                    print("Não é possível a doação pois a idade está fora do permitido")
                elif(idade > 60):
                    doador = input("Já doou sangue (S/N): ")
                    if(doador == "S" or doador == "s"):
                        #Solicitando peso
                        peso = float(input("Digite o peso em quilogramas: "))
                        #Verificando condicional de peso
                        if(peso < 50):
                            print("Não é possível a doação, pois a doadora está abaixo do peso mínimo.")
                        else:
                            #Verificando se está com febre
                            febre = input("Está com febre (S/N): ")
                            if(febre == "S" or febre == "s"):
                                print("Não é possível a doação, pois a doadora está com febre.")
                            elif(febre == "N" or febre == "n"):
                                print("A doação é possível.")
                            else:
                                #Digitou valor inválido, finalizando programa
                                print("Valor inválido.") 
                    elif(doador == "N" or doador == "n"):
                        print("Não é possível a doação, pois a doadora nunca doou antes dos 60 anos.")
                    else:
                        #Digitou valor inválido, finalizando programa
                        print("Valor inválido.")
                else:
                    #Solicitando peso
                    peso = float(input("Digite o peso em quilogramas: "))
                    #Verificando condicional de peso
                    if(peso < 50):
                        print("Não é possível a doação, pois a doadora está abaixo do peso mínimo.")
                    else:
                        #Verificando se está com febre
                        febre = input("Está com febre (S/N): ")
                        if(febre == "S" or febre == "s"):
                            print("Não é possível a doação, pois a doadora está com febre.")
                        elif(febre == "N" or febre == "n"):
                            print("A doação é possível.")
                        else:
                            #Digitou valor inválido, finalizando programa
                            print("Valor inválido.")
            elif(tempo == "N" or tempo == "n"):
                print("Não é possível a doação, pois a doadora está amamentando.") 
            else:
                #Digitou valor inválido, finalizando programa
                print("Valor inválido.")
        elif(amamentando == "N" or amamentando == "n"):
            #Solicitando idade
            idade = int(input("Digite a idade: "))
            #Verificando condicionais de idade
            if(idade < 16 and idade > 69):
                print("Não é possível a doação pois a idade está fora do permitido")
            elif(idade > 60):
                doador = input("Já doou sangue (S/N): ")
                if(doador == "S" or doador == "s"):
                    #Solicitando peso
                    peso = float(input("Digite o peso em quilogramas: "))
                    #Verificando condicional de peso
                    if(peso < 50):
                        print("Não é possível a doação, pois a doadora está abaixo do peso mínimo.")
                    else:
                        #Verificando se está com febre
                        febre = input("Está com febre (S/N): ")
                        if(febre == "S" or febre == "s"):
                            print("Não é possível a doação, pois a doadora está com febre.")
                        elif(febre == "N" or febre == "n"):
                            print("A doação é possível.")
                        else:
                            #Digitou valor inválido, finalizando programa
                            print("Valor inválido.") 
                elif(doador == "N" or doador == "n"):
                    print("Não é possível a doação, pois a doadora nunca doou antes dos 60 anos.")
                else:
                    #Digitou valor inválido, finalizando programa
                    print("Valor inválido.")
            else:
                #Solicitando peso
                peso = float(input("Digite o peso em quilogramas: "))
                #Verificando condicional de peso
                if(peso < 50):
                    print("Não é possível a doação, pois a doadora está abaixo do peso mínimo.")
                else:
                    #Verificando se está com febre
                    febre = input("Está com febre (S/N): ")
                    if(febre == "S" or febre == "s"):
                        print("Não é possível a doação, pois a doadora está com febre.")
                    elif(febre == "N" or febre == "n"):
                        print("A doação é possível.")
                    else:
                        #Digitou valor inválido, finalizando programa
                        print("Valor inválido.")
        else:
            #Digitou valor inválido, finalizando programa
            print("Valor inválido.")        
    elif(gravida == "S" or gravida == "s"):
        print("Não é possível a doação, pois a doadora está grávida.")
    else:
        #Digitou valor inválido, finalizando programa
        print("Valor inválido.")
elif(sexo == "M" or sexo == "m"):
    #Solicitando idade
    idade = int(input("Digite a idade: "))
    #Verificando condicionais de idade
    if(idade < 16 and idade > 69):
        print("Não é possível a doação, pois a idade está fora do permitido")
    elif(idade > 60):
        doador = input("Já doou sangue (S/N): ")
        if(doador == "S" or doador == "s"):
            #Solicitando peso
            peso = float(input("Digite o peso em quilogramas: "))
            #Verificando condicional de peso
            if(peso < 60):
                print("Não é possível a doação, pois o doador está abaixo do peso mínimo.")
            else:
                #Verificando se está com febre
                febre = input("Está com febre (S/N): ")
                if(febre == "S" or febre == "s"):
                    print("Não é possível a doação, pois o doador está com febre.")
                elif(febre == "N" or febre == "n"):
                    print("A doação é possível.")
                else:
                    #Digitou valor inválido, finalizando programa
                    print("Valor inválido.") 
        elif(doador == "N" or doador == "n"):
            print("Não é possível a doação, pois o doador nunca doou antes dos 60 anos.")
        else:
            #Digitou valor inválido, finalizando programa
            print("Valor inválido.")
    else:
        #Solicitando peso
        peso = float(input("Digite o peso em quilogramas: "))
        #Verificando condicional de peso
        if(peso < 60):
            print("Não é possível a doação, pois o doador está abaixo do peso mínimo.")
        else:
            #Verificando se está com febre
            febre = input("Está com febre (S/N): ")
            if(febre == "S" or febre == "s"):
                print("Não é possível a doação, pois o doador está com febre.")
            elif(febre == "N" or febre == "n"):
                print("A doação é possível.")
            else:
                #Digitou valor inválido, finalizando programa
                print("Valor inválido.")
else:
    #Digitou valor inválido, finalizando programa
    print("Valor inválido.")
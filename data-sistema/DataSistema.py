from datetime import datetime

def mesAtual():
    mes = 7
    data_atual = datetime.today().strftime('%Y-%m-%d')
    data_atual = data_atual.split("-")
    mes_atual = int(data_atual[1])
    print(data_atual)
    print(mes_atual)
    if(mes != mes_atual):
        mes = mes_atual
        print("Mês diferente do atual")
        return False
    else:
        print("Mês retornado é o atual")
        return True

mesAtual()
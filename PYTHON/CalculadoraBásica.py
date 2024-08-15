a = 1
b = 1
calcular = input("Deseja realizar uma/outra operação? (S/N): ")
while calcular == "S":
    print("Adição")
    print("Subtração")
    print("Multiplicação")
    print("Divisão")
    print("Sair")
    operacao = input("Selecione a operação a ser realizada (digite 0 durante a operação para trocar de operação): ")
    if operacao == "Adição":
        while a != 0:
            a = int(input("Digite um número: "))
            while b != 0:
                b = int(input("Digite outro número: "))
                x = a + b
                print("A soma é igual a ", x)
    if operacao == "Subtração":
        while a != 0:
            a = int(input("Digite um número: "))
            while b != 0:
                b = int(input("Digite outro número: "))
                x = a - b
                print("A subtração é igual a ", x)
    if operacao == "Multiplicação":
        while a != 0:
            a = int(input("Digite um número: "))
            while b != 0:
                b = int(input("Digite outro número: "))
                x = a * b
                print("A multiplicação é igual a ", x)
    if operacao == "Divisão":
        while a != 0:
            a = int(input("Digite um número: "))
            while b != 0:
                b = int(input("Digite outro número: "))
                x = a / b
                print("A divisão é igual a ", x)
    if operacao == "Sair":
        print("Foi bom calcular com você =)")
        break
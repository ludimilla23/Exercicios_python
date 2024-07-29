menu = {}
menu['1'] = "Soma"
menu['2'] = "Subtração"
menu['3'] = "Multiplicação"
menu['4'] = "Divisão"
menu['5'] = "Sair"

while True:
    options = menu.keys()
    options = sorted(options)  

    for entry in options:
        print(entry, menu[entry])

    selection = input("Por favor selecione uma operação: ")  # use input() instead of raw_input() for Python 3

    if selection == '1':
        a, b = map(float, input("Digite os dois números: ").split())
        resultado = a + b
        print(f"O resultado é: {resultado}")
    elif selection == '2':
        a, b = map(float, input("Digite os dois números: ").split())
        resultado = a - b
        print(f"O resultado é: {resultado}")
    elif selection == '3':
        a, b = map(float, input("Digite os dois números: ").split())
        resultado = a * b
        print(f"O resultado é: {resultado}")
    elif selection == '4':
        a, b = map(float, input("Digite os dois números: ").split())
        if b != 0:
            resultado = a / b
            print(f"O resultado é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    elif selection == '5':
        break
    else:
        print("Unknown Option Selected!")

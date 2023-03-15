# Calculadora Simples

while True:

    print("\nDigite o Primeiro Número: ")
    numero1 = int(input())

    print("\nDigite o Segundo Número: ")
    numero2 = int(input())

    print("\nQual Operação Voçê Deseja Utilizar? \n+ Para Soma \n- Para Subtração \n* Para Multiplicação \n/ Para Divisão\n")
    operador = input()

    if operador == '+':
        resultado = numero1 + numero2
        print("\nA Soma é:")
        print(resultado)
    elif operador == '-':
        resultado = numero1 - numero2
        print("\nA Subtração é:")
        print(resultado)
    elif operador == '*':
        resultado = numero1 * numero2
        print("\nA Multiplicação é:")
        print(resultado)
    elif operador == '/':
        resultado = numero1 / numero2
        print("\nA Divisão é:")
        print(resultado)
    else:
        print("\nOperador Inválido")

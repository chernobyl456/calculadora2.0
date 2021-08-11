import math

titulo = str("Calculadora 2.0")
print('\033[1;32m{:=^30}\033[m'.format(titulo))

power = True
n1 = float(input ("Digite um valor: "))
operacao = 0

while power:
    opcao =str(input('''\033[1;36m
[+]soma
[-]subtração
[*]multiplicação
[/]Divisão
[0]sair
\033[m'''))
    if opcao == '+':
        n2 = float(input("Digite outro valor: "))
        operacao = n1 + n2
        print('\033[1;33m=\033[m' * 60)
        print(f'\033[1;35m{n1} + {n2} = {operacao}\033[m')
    elif opcao == '-':
        n2 = float(input("Digite outro valor: "))
        operacao = n1 - n2
        print('\033[1;33m=\033[m' * 60)
        print(f'\033[1;35m{n1} - {n2} = {operacao}\033[m')

    elif opcao == '*':
        n2 = float(input("Digite outro valor: "))
        operacao = n1 * n2
        print('\033[1;33m=\033[m' * 60)
        print(f'\033[1;35m{n1} * {n2} = {operacao}\033[m')

    elif opcao == '/':
        n2 = float(input("Digite outro valor: "))
        operacao = n1 / n2
        print('\033[1;33m=\033[m' * 60)
        print(f'\033[1;35m{n1} / {n2} = {operacao}\033[m')

    elif opcao == '0':
        power = False

    else:
        print('opção invalida... tente novamente')

    n1 = operacao
    print('\033[1;33m=\033[m' * 60)

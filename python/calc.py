import os

clear = lambda: os.system('clear')

def soma(n1, n2):
    return n1+n2 

def subtracao(n1, n2):
    return n1-n2

def multiplicacao(n1, n2):
    return n1*n2 

def divisao(n1, n2):
    if n2 == 0:
        print("é impossível dividir por zero")
    else:     
        return n1/n2 

def exponenciacao(n1, n2):
    return n1**n2  


escolha = True
while escolha == True:
    print("WATASHI NO CALCULATOR NO YOKOSO!!")
    print("0: SOMA")
    print("1: SUBTRAÇÃO")
    print("2: MULTIPLICAÇÃO")
    print("3: DIVISÃO")
    print("4: EXPONENCIAÇÃO")

    print("ESCOLHA UMA OPERAÇÃO ONEGAISHIMASU!!!")
    escolha = input()
    clear()

    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))

    if escolha == "0":
        resultado = soma(n1, n2)
    elif escolha == "1":
        resultado = subtracao(n1, n2)
    elif escolha == "2":
        resultado = multiplicacao(n1, n2)
    elif escolha == "3":
        resultado = divisao(n1, n2)
    elif escolha == "4":
        resultado = exponenciacao(n1, n2)
    else:
        print("Escolha inválida")


    print(resultado)

    sn = input("Deseja fazer uma nova escolha? 's' or 'n'")
    clear()
    while True:
        if sn == "n":
            escolha = False
            break
        elif sn == "s":
            clear()
        else:
            print("Escolha inválida")
            sn = input("Deseja fazer uma nova escolha? 's' ou 'n'")

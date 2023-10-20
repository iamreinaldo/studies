import os

clear = lambda: os.system('clear')

listaDeCarros = {0:["Chevrolet Tracker", 120],1:["Chevrolet Onix", 90], 2:["Chevrolet Spin",150], 3:["Hyundai HB20", 85], 4:["Hyundai Tucson", 120], 5:["Fiat Uno", 60], 6:["Fiat Mobi", 70], 7:["Fiat Pulse", 130]}
carrosAlugados = {}

# , 

def mostrarCarros():
    for i in listaDeCarros:
        print("[{}] - {} - R$ {} /dia".format((i),listaDeCarros[i][0], listaDeCarros[i][1]))


def alugarCarro(carro):
    for i in listaDeCarros: 
        if carro == i:

            carrosAlugados[i] = listaDeCarros.pop(i)
            return print("Carro alugado com sucesso!\n")


def mostrarCarrosAlugados():
    for i in carrosAlugados:
        print("[{}] - {} - R$ {} /dia".format((i),carrosAlugados[i][0], carrosAlugados[i][1]))

def devolverCarro(carro):
    for i in carrosAlugados:
        if carro == i:
            listaDeCarros[i] = carrosAlugados.pop(i)
            return print("Carro devolvido com sucesso")


while True:
    print("===============================")
    print("Bem vindos à locadora de carros!")
    print("===============================")
    print("O que deseja fazer?")
    escolha = input("1 - Mostrar carros | 2 - Alugar um carro | 3 - Devolver um carro | 4 - Para sair\n")
    clear()

    if escolha == "1":
        mostrarCarros()
        segundaEscolha = input("\nQualquer botão para ir para o Menu iniciar | 2 - Finalizar\n")
        clear()
        if segundaEscolha == "2": 
            break
             

    elif escolha == "2":
        mostrarCarros()
        carro = int(input("Escolha o carro:\n"))
        dias = int(input("Quantos dias deseja alugar o carro?\n"))
        total = dias * listaDeCarros[carro][1]
        decisao = input("O valor total é R${}, deseja alugar? s ou n\n".format(total))
        if decisao == "s":
            alugarCarro(carro)
        elif decisao == "n":
            clear()
            print("Agradecemos o seu contato")
        else:
            print("Opção inválida")
        segundaEscolha = input("\nQualquer botão para ir para o Menu iniciar | 2 - Finalizar\n")
        clear()
        if segundaEscolha == "2": 
            break

    elif escolha == "3":
        if len(carrosAlugados) == 0:
            print("Não há carros para devolver")
            segundaEscolha = input("\nQualquer Botão para ir para o Menu iniciar | 2 - Finalizar\n")
            clear()
            if segundaEscolha == "2": 
                break
        else:
            mostrarCarrosAlugados()
            print("\n===============================")
            carroDevolvido = int(input("Qual carro deseja devolver?"))
            devolverCarro(carro)
            segundaEscolha = input("\nQualquer Botão para ir para o Menu iniciar | 2 - Finalizar\n")
            clear()
            if segundaEscolha == "2": 
                break
    elif escolha == "4":
        break




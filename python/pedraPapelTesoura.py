import os
import random
clear = lambda: os.system("clear")

pontoUser = 0
pontoPc = 0




while True:
    print("Jokenpo no yokoso!!")
    print("====================")
    print("PLACAR:")
    print("Seus pontos: {}".format(pontoUser))
    print("Meus pontos: {}".format(pontoPc))
    print("====================")
    userChoice = int(input("0 - Pedra | 1 - Papel | 2 - Tesoura | 3 - Para fechar o jogo\n"))
    pcChoice = random.randint(0,2)
    clear()
    if userChoice == 0 and pcChoice == 0:
        print("Você escolheu Pedra e eu também")
        print("Empate")
        print("====================")
        escolha = input("0 - Para sair | Qualquer botão para jogar novamente")
        if escolha == 0:
            clear()
            break
    
    elif userChoice == 0 and pcChoice == 1:
        print("Você escolheu Pedra e eu papel")
        print("Você perdeu")
        pontoPc +=1
        print("====================")
        escolha = input("0 - Para sair | Qualquer botão para jogar novamente")
        if escolha == 0:
            clear()
            break
    
    elif userChoice == 0 and pcChoice == 2:
        print("Você escolheu Pedra e eu tesoura")
        print("Você venceu")
        pontoUser +=1
        print("====================")
        escolha = input("0 - Para sair | Qualquer botão para jogar novamente")
        if escolha == 0:
            clear()
            break
    elif userChoice == 1 and pcChoice == 0:
        print("Você escolheu papel e eu pedra")
        print("Você venceu")
        pontoUser +=1
        print("====================")
        escolha = input("0 - Para sair | Qualquer botão para jogar novamente")
        if escolha == 0:
            clear()
            break
    elif userChoice == 1 and pcChoice == 1:
        print("Você escolheu papel e eu também")
        print("Empate")
        print("====================")
        escolha = input("0 - Para sair | Qualquer botão para jogar novamente")
        if escolha == 0:
            clear()
            break
    elif userChoice == 1 and pcChoice == 2:
        print("Você escolheu papel e eu tesoura")
        print("Você perdeu")
        pontoPc +=1
        print("====================")
        escolha = input("0 - Para sair | Qualquer botão para jogar novamente")
        if escolha == 0:
            clear()
            break

    elif userChoice == 2 and pcChoice == 0:
        print("Você escolheu tesoura e eu pedra")
        print("Você perdeu")
        pontoPc +=1
        print("====================")
        escolha = input("0 - Para sair | Qualquer botão para jogar novamente")
        if escolha == 0:
            clear()
            break

    elif userChoice == 2 and pcChoice == 1:
        print("Você escolheu tesoura e eu papel")
        print("Você venceu")
        pontoUser +=1
        print("====================")
        escolha = input("0 - Para sair | Qualquer botão para jogar novamente")
        if escolha == 0:
            clear()
            break

    elif userChoice == 2 and pcChoice == 2:
        print("Você escolheu tesoura e eu também")
        print("Empate")
        print("====================")
        escolha = input("0 - Para sair | Qualquer botão para jogar novamente")
        if escolha == 0:
            clear()
            break

    elif userChoice == 3:
        break


    
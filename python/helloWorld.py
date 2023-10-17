def calculaMedia(nome, nota1, nota2):
    media = (nota1+nota)/2
    if media > 7:
        print("Parabéns {}, sua média foi {} e você foi aprovado!".format(nome, media)
    elif media == 10:
        print("PARABÉNS {}, VOCÊ FECHOU A MÉDIA!!".format(nome)
    else:
        print("Sinto muito {}, você foi reprovado com a média {}.".format(nome, media)



calculaMedia(input(),input(),input())
import random
vidas = 3
rival = 3
while True:

    opcoes = ["PEDRA", "PAPEL", "TESOURA"]
    escolha = random.choice(opcoes)
    player=input("PEDRA, PAPEL OU TESOURA? ").upper()
    
    if player == escolha:
        print("EMPATOU")
    elif player == ("PEDRA") and escolha ==("TESOURA"):
        rival -= 1
        print("VOCÊ GANHOU")
    elif player == ("PEDRA") and escolha ==("PAPEL"):
        vidas -= 1
        print("VOCÊ PERDEU")
    elif player == ("PAPEL") and escolha ==("PEDRA"):
        rival -= 1
        print("VOCÊ GANHOU")
    elif player == ("PAPEL") and escolha ==("TESOURA"):
        vidas -= 1
        print("VOCÊ PERDEU")
    elif player == ("TESOURA") and escolha ==("PAPEL"):
        rival -= 1
        print("VOCÊ GANHOU")
    elif player == ("TESOURA") and escolha ==("PEDRA"):
        vidas -= 1
        print("VOCÊ PERDEU")
    print("A MÁQUINA ESCOLHEU",escolha)
    print("VOCÊ POSSUI",vidas,"VIDAS")
    print("O RIVAL POSSUI",rival,"VIDAS")
    sair=str(input("SAIR? [S/N]")).upper()
    if sair ==("S"):
        break
    if vidas < 1:
        print("SEM VIDAS")
        break
    if rival < 1:
        print("VOCÊ É CAMPEÃO!")
        break
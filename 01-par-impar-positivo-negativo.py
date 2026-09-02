while True:
    n=int(input("É IMPAR OU PAR? DIGITE O NÚMERO: "))
    if n % 2 == 0:
     print("PAR")
    else:
        print("IMPAR")

    if n > 0:
         print("POSITIVO")
    elif n == 0:
        print("ZERO")
    else:
        print("NEGATIVO")

    if n % 5 == 0:
        print("MULTIPLO DE 5")
    else:
        print("NÃO É MULTIPLO DE 5")
    sair=str(input("DESEJA SAIR? (S/N): "))
    if sair.upper() == ("S"):
        break    
    
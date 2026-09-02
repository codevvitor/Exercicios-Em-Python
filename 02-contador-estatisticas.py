numero = []
while True:
    n = int(input("DIGITE UM NÚMERO: "))
    numero.append(n)          
    
    sair = input("SAIR? (S/N): ")
    if sair.upper() == "S":
        break                  


print("QUANTIDADE: ",len(numero))
print("NÚMERO MAIOR: ",max(numero))
print("NÚMERO MENOR: ",min(numero))

pares = 0
impares = 0
for numero_da_lista in numero:
    if numero_da_lista % 2 == 0:
        pares += 1
    else:
        impares += 1
        
print(pares,"NÚMEROS PARES")
print(impares,"NÚMEROS IMPARES")
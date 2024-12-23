from random import randrange

lista = []
npasse = randrange(1,50)
print(npasse)
cont = 3
while True:
    passe = int(input("Digite seu passe: "))
    lista.append(passe) if passe not in lista and passe == npasse else print("Seu passe está errado")
    if npasse in lista:
        print("Pode entrar na festa")
        break
    cont -= 1
    print(f"voce tem mais {cont} tentativas")
    if cont == 0:
       print("Pode entrar não")
       break



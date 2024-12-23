import random

while True:
    pensar = random.randint(1, 5)  
    pc = int(input("Pensei em um número de 1 a 5, tente adivinhar: "))
    if pc == pensar:
        print("Isso mesmo, certa resposta")
        break
    else:
        print("Número errado")
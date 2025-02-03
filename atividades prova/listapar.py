#Crie uma lista com 10 números inteiros aleatórios e use um loop para exibir apenas os números pares.

import random

lista = []
listapar = []
for x in range(0,10):
    aleatorio = random.randint(0,100)
    lista.append(aleatorio)
    if aleatorio % 2 == 0:
        listapar.append(aleatorio)
print(lista)
print(listapar)

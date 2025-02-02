#Crie um programa que peça 5 números ao usuário, armazene-os em uma tupla e informe qual é o maior e o menor valor digitado.

lista = []
tupla = ()

for x in range(0,5):
    numeros = int(input("Digite um numero: "))
    lista.append(numeros)

tupla = tuple(lista)
print(f"O maior número é o {max(tupla)}, e o menor é {min(tupla)}")
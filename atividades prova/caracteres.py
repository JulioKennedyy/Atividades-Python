#Escreva um programa que peça ao usuário para digitar uma frase e conte quantas palavras possuem mais de 5 caracteres.

frase = str(input("Digite uma frase: "))
nova = frase.split(" ")
cont = 0

for palavra in nova:
    cont += 1 if len(palavra) > 5 else 0

print(f"A quantidade de palavras com mais de 5 caracteres é: {cont}")
lista = []
while True:
    numero = input("Digite um número, caso queira parar digite x: ")
    if numero.lower() == "x":
        break
    else:
        numero = int(numero)
    lista.append(numero)
if lista:
    media = sum(lista) / len(lista)
    print(f"A média dos números digitados é: {media}")
else:
    print("Nenhum número foi digitado. Não é possível calcular a média.")



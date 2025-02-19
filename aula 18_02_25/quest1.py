lista = []

while True:
    numero = input("Digite um numero para ser adicionado a lista: ")
    lista.append(numero)
    continuar = str(input("Aperte x para parar a execução: ")).lower()
    if continuar == "x":
        break
    
print(lista)
def soma_inteiros(lista):
    soma = 0
    for x in lista:
        try:
            xy = int(x)
            soma += xy
        except ValueError:
            print("string")
    return soma


print(soma_inteiros(lista))
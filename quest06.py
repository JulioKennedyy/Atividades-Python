lista = []
inteiros = int(input("Digite quantos números inteiros terão: "))
for x in range(inteiros):
    numeros = int(input("Digite um número inteiro: "))
    lista.append(numeros)

verificados = []

for numeros in lista:
    if numeros not in verificados:
        contagem = lista.count(numeros)
    print(f"o numero {numeros} aparece: {contagem} vezes")
    verificados.append(numeros)

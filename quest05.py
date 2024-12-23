lista = []
positivos = []
numeros = int(input("Digite um valor: "))
for x in range(numeros):
    lista.append(x)
    if x > 0:
        positivos.append(x+1)

if not positivos:
    print("Sem números positivos")
else:
    media = sum(positivos) / len(positivos)
    print(f"Os números positivos são: {positivos} e sua média é: {media}")
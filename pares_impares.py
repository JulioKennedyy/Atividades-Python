lista = []
pares = []
impares = []
while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    if num % 2 != 0:
        impares.append(num)
    con = str(input("Quer continuar?(S/N): "))
    if con in "Nn":
        break

print(lista)
print(pares)
print(impares)
lista = []
while True:
    num = int(input("Digite um número: "))
    if num not in lista:
        lista.append(num)
    con = str(input("Quer continuar?(S/N): "))
    if con in "Ss":
        continue
    elif con in "Nn":
        break
    elif not con in "Ss" or con in "Nn":
        print("Digite uma das opções(S/N)")
        continue

lista.sort()
print(lista)
menor_de_idade = []
adulto = []
idoso = []
quantidade_idade = int(input("Digite quantas idades quer digitar: "))
for x in range(quantidade_idade):
    idade = int(input("Digite as idades: "))
    if idade < 18:
        menor_de_idade.append(idade)
    elif idade < 0:
        print("idade invalida")
    if idade >= 18 and idade < 60:
        adulto.append(idade)
    if idade >= 60 and idade < 150:
        idoso.append(idade)
    if idade >= 150:
        print("Matusalém")

print(f"Os menores de idade são: {menor_de_idade}, os adultos são: {adulto}, e os idosos são: {idoso}")
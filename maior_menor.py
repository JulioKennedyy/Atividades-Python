lista = []
dic = {"Maiores": [], "Menores": []}

while True:
    tupla = (str(input("Digite seu nome: ")), int(input("Digite sua idade: ")))
    lista.append(tupla)
    confirmar = str(input("Quer continuar? (digite x para sair): "))
    if confirmar == "x" or confirmar == "X":
        break
    else:
        continue

for pessoa in lista:
    nome, idade = pessoa
    dic["Maiores"].append(nome) if idade >= 18 else dic["Menores"].append(nome)


print(dic)
dic = {}
while True:
    lista = []
    tupla = str(input("Digite seu nome: ")), float(input("Digite sua primeira nota: ")), float(input("Digite sua segunda nota: ")), float(input("Digite sua terceira nota: "))
    lista.append(tupla)

    
    for aluno in lista:
        nome, nota1, nota2, nota3 = aluno
        total = (nota1 + nota2 + nota3)/3
        if total >= 7:
            dic[nome] = "Aprovado"
        else:
            dic[nome] = "Reprovado"
    parar = input("Digite X para parar: ")
    if parar in "xX":
        break
    else:
        continue

print(dic)
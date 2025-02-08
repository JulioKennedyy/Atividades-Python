# Faça um programa que receba dois números do usuário, coloque os mesmos numa tupla, e passe a tupla para uma função que retorna 0 se o primeiro valor é maior que o segundo, 1, se o primeiro valor é menor que o segundo e 2, caso os números sejam iguais.

def tuplinha(tupla):
    for valor in tupla:
        if tupla[0] > tupla[1]:
            return 0
        elif tupla[1] > tupla[0]:
            return 1
        else:
            return 2


tupla = (int(input("Digite o primeiro numero: ")), int(input("Digite o segundo numero: ")))
print(tuplinha(tupla))


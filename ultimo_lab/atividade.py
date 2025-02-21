# Dado o arquivo anexo com transações de uma conta bancária, faça um programa que leia o arquivo, calcule o saldo final da pessoa e o imprima na tela, depois salve o total por categoria em outro arquivo, numa subpasta no formato (YYYYMM), onde Y é o ano e M é o mês das transações.

try:
    with open("Júlio Kennedy dos Santos Silva - transacoes.csv")  as arquivo:
        texto = arquivo.readlines()
        valor = 0
        for valores in texto:
            novos = valores.strip().split(";")
            novos[3] = int(novos[3])
            novos[3] = float(novos[3])
            novos[3] += valor
        print(valor)

        

except Exception as ex:
    print("Deu ruim", ex)
# Dado o arquivo anexo com transações de uma conta bancária, faça um programa que leia o arquivo, calcule o saldo final da pessoa e o imprima na tela, depois salve o total por categoria em outro arquivo, numa subpasta no formato (YYYYMM), onde Y é o ano e M é o mês das transações.

try:
    with open("Júlio Kennedy dos Santos Silva - transacoes.csv", "r")  as arquivo:
        texto = arquivo.readlines()
        valor = 0
        lista = []
        lista_atualizada = []
        for valores in texto[1:]:
            novos = valores.strip().split(";")
            lista.append(novos[3])
        for num in lista:
            num2 = num.replace(",", ".")
            num2 = float(num2)
            lista_atualizada.append(num2)
        print(f"Seu saldo final é: {sum(lista_atualizada)}")

        

except Exception as ex:
    print("Deu ruim", ex)
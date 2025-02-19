from funcc import *
lista = []

while True:
    try:
        escolha = str(input("Digite 1 caso queira cadastrar uma conta\nDigite 2 caso queira transferir\nDigite 3 para sair\n: "))
        match escolha:
            case("1"):
                try:
                    nome = str(input("Digite o nome do titular: ")).lower().strip()
                    numero = int(input("Digite o numero do titular: "))
                    valor = float(input("Digite o dinheiro da conta: "))
                    dicionario = {"Nome": nome, "Número": numero, "Valor": valor}
                    lista.append(dicionario)
                except ValueError:
                    print("Tipo de dado recebido invalido")
            case("2"):
                tipo = str(input("Quer tranferir por numero da conta(n) ou nome da conta(c)?: "))
                match tipo:
                    case("n"):
                        try:
                            numero1 = int(input("Numero da conta que vai enviar: "))
                            numero2 = int(input("Numero da conta que vai receber: "))
                        except ValueError:
                            print("Tipo de dado recebido invalido")
                    case("c"):
                        transfe1 = str(input("Digite o nome da conta que vai enviar: "))
                        transfe2 = str(input("Digite o nome da conta que vai receber: "))
                quantidade = float(input("Digite a quantidade que deseja enviar: "))
                if tipo == ("c"):
                    for x in lista:
                        if x["Nome"] == transfe1:
                            valor1 = x["Valor"]
                            for x in lista: 
                                if x["Nome"] == transfe2:
                                    valor2 = x["Valor"]
                                    print(transferir(valor1,quantidade,valor2))
                elif tipo == ("n"):
                    for x in lista:
                        if x["Número"] == numero1:
                            valor1 = x["Valor"]
                            for x in lista: 
                                if x["Número"] == numero2:
                                    valor2 = x["Valor"]
                                    print(transferir(valor1,quantidade,valor2))
    except ValueError:
        print("Algum dado fornecido é invalido")
    except Exception as ex:
        print("Erro,", ex)
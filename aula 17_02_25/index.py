from func import *

lista = []
while True:
    try:
        escolha = str(input("Digite 1 caso queira cadastrar um motorista\nDigite 2 caso queira listar todos os motoristas\nDigite 3 para sair\n: "))
        match escolha:
            case("1"):
                nome = str(input("Digite seu nome: "))
                idade = str(input("Digite sua data de nascimento: "))
                idade2 = verifi_idade(idade)
                cnhh = cnh()
                dicionario = {"Nome": nome, "Idade": idade2, "Cnh": cnhh}
                lista.append(dicionario)
            
            case("2"):
                for indice, dici in enumerate(lista):
                    print(f"{indice}: {dici}")
            
            case("3"):
                break

    except ValueError:
        print("Digito invalido")

    except Exception as ex:
        print("deu ruim", ex)
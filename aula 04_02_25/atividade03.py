#Faça um programa que cadastre mercadorias em uma lista de dicionários. Em seguida o usuário poderá listar os produtos cadastrados e também dar um aumento percentual em determinado projeto, passando seu identificador e o valor percentual.

lista = []

def aumentar_percentual(porcentagem, quantidade):
    resultado = quantidade * porcentagem/100 + quantidade
    return resultado


while True:
    mercadoria = str(input("Digite o nome da mercadoria: ")).lower()
    quantidade = int(input("Digite a quantidade da mercadoria: "))
    lista.append({mercadoria: quantidade})
    tela = int(input("Digite (1) caso queira listar os itens\nDigite (2) caso queira dar um aumento em porcentagem em algum item\nDigite (3) para parar a aplicação \n :"))
    match tela:
        case(1):
            print(lista)
        case(2):
            identificador = str(input("Digite a mercadoria que deseja aumentar: " )).lower()
            for x in lista:
                if x == identificador:
                    print("Mercadoria não existe")
                    continue
            else:
                porcentagem = int(input("Digite a porcentagem a ser adicionada: "))
                for produto in lista:
                    if produto.get(identificador):
                        print(aumentar_percentual(porcentagem, produto.get(identificador)))
        case(3):
            break
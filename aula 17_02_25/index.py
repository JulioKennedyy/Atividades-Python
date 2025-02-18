from func import *

lista = []
while True:
    try:
        escolha = str(input("Digite 1 caso queira cadastrar um motorista\nDigite 2 caso queira listar todos os motoristas\nDigite 3 para sair\n: "))
        match escolha:
            case("1"):
                nome = str(input("Digite seu nome: "))
                idade = str(input("Digite sua data de nascimento: "))
estoque = {}
while True:
    menu = input("Digite o que deseja fazer(Digite 1 para adicionar, 2 para remover, 3 para atualizar ou 4 para sair): ")
    if menu == ("4"):
        break
    match menu:
        case("1"):
            adicionar = input("Digite o item: ").lower
            quantidade = int(input("Digite a quantidade: "))
            estoque[adicionar] = quantidade
        case("2"):
            remover = input("Digite o item que deseja remover: ")
            if not estoque:
                print("Estoque vazio")
            elif remover not in estoque:
                print("Não está no estoque")
            else:
                estoque.pop(remover)
        case("3"):
            atualizar = input("Digite o que deseja atualizar a quantidade: ")
            novaquanti = int(input("Digite a nova quantidade: "))
            if estoque == False:
                print("Estoque vazio")
            elif atualizar not in estoque:
                print("Não está no estoque")
            else:
                estoque[atualizar] = novaquanti
       

print(estoque)
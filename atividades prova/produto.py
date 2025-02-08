dic = {}

while True:
    tupla1 = input("Digite o nome do produto: ")
    tupla2 = input("Digite a quantidade do produto: ")
    dic[tupla1] = [tupla2]
    sair = str(input("Digite (x) caso queira sair: ")).lower()
    if sair == "x":
        break
print(dic)

def busca_preco(nome):
    for c in dic:
        if c == nome:
            return dic[nome]
        elif nome not in dic:
            return "Item não existente"
    
eu = busca_preco("coca")
print(eu)
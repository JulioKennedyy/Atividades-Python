# Dado o seguinte dicionário de produtos e seus respectivos preços:
# produtos = { "arroz": 10.0, "feijão": 8.5, "macarrão": 5.0, "carne": 35.0 }
# Implemente uma função chamada aplica_desconto que receba o dicionário e um valor percentual de desconto e retorne um novo dicionário com os produtos e seus preços com o desconto aplicado

produtos = { "arroz": 10.0, "feijão": 8.5, "macarrão": 5.0, "carne": 35.0 }

def aplica_desconto(dicionario: str, desconto: int):
    novoproduto = {}
    for item, valor in dicionario.items():
        novoproduto[item] = valor * desconto / 100 + valor
    return novoproduto

print(aplica_desconto(produtos, 100))

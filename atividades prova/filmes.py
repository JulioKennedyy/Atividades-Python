#Crie um dicionário vazio filmes = {}. Utilize o nome de um filme como chave. E, como valor, outro dicionário contendo o vilão e o ano em que o filme foi lançado. Preencha 5 filmes.

filmes = {}

def preencher_filmes(nome, *kwargs):
    for x in range(0,5):
        filmes[nome] = kwargs
    return filmes

for c in range(0,5):
    nome = str(input("Digite o nome do filme: "))
    vilao = str(input("Digite o nome do vilão: "))
    ano = int(input("Digite o ano do filme: "))
    print(preencher_filmes(nome, {vilao: ano}))
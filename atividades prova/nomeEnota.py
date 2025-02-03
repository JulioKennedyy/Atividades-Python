#Crie um dicionário para armazenar o nome e a nota de 5 alunos. Depois, exiba os nomes dos alunos que tiveram nota maior que 7.

dic = {}

for x in range(0,5):
    nome = str(input("Digite o nome do aluno: "))
    nota = float(input("Digite a nota do aluno: "))
    dic[nome] = nota

for nome, nota in dic.items():
    if nota >= 7.0:
        print(nome)

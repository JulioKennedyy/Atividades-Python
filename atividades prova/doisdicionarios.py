# Dados os dois dicionários abaixo, faça um programa que iguale as chaves contidas neles. O valor da chave que ele não possui deve ser o mesmo do outro dicionário.
# aluno1 = {
#     “nome”: “Aluno 1”,
#     “idade”: 15,
#     “serie”: 2
# }
# aluno2 = {
#     “nome”: “Aluno 2”,
#     “nacionalidade”: “brasileiro”,
#     “serie”: 2,
#     “altura”: 1.70
# 	}

aluno1 = {
    "nome": "Aluno 1",
    "idade": 15,
    "serie": 2
}

aluno2 = {
    "nome": "Aluno 2",
    "nacionalidade": "brasileiro",
    "serie": 2,
    "altura": 1.70
}

for key, value in aluno1.items():
    if key not in aluno2:
        aluno2[key] = value
for key, value in aluno2.items():
    if key not in aluno1:
        aluno1[key] = value

print(aluno1)
print(aluno2)

"""while True:
    nota = int(input("Digite um número de 0 a 10: "))
    if nota not in (1,2,3,4,5,6,7,8,9,10):
        print("Nota inválida, digite novamente")
        continue
    else:
        print(f"Número {nota} válido.")
        break
print("Cabô")"""

while True:
    nome = str(input("Digite seu nome: "))
    senha = str(input("Digite sua senha: "))
    if nome == senha:
        print("O nome não pode ser igual a senha, faz de novo")
        continue
    else:
        print("Nome e senha corretos.")
        break


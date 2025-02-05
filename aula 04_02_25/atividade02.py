#Faça um programa que solicite os dados nome, idade e cpf (utilizando pontuação) de vários contato e só permita salvar o usuário em uma lista de dicionários se os dados foram preenchidos e se o cpf possuir 11 dígitos excluindo pontos e traços. O usuário também poderá listar os usuários cadastrados.

lista = []

def validar_cpf(cpf):
        sem_ponto = cpf.replace(".", "")
        sem_linha = sem_ponto.replace("-", "")
        if len(sem_linha) == 11:
             valor = True
             return valor
        else:
            valor = False
            return valor
        
while True:
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    cpf = str(input("Digite seu CPF: ")).strip()
    if nome == False or idade == False:
        print("Dados não preenchidos")
        continue
    if validar_cpf(cpf) == True:
        lista.append({"nome": nome, "idade": idade, "cpf": cpf})
        sair = str(input("Quer cadastrar outro usuario? (digite x caso não): ")).lower()
        if sair == "x":
            break
    else:
         print("Cpf invalido")
         continue
       
print(lista)
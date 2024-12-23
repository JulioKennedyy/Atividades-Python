num = int(input("Digite um número: "))
atual = 0 
proximo = 1
soma = 0
for i in range(num):
    print(atual)
    soma += atual
    resultado = atual + proximo
    atual = proximo
    proximo = resultado
print(f'A soma da sequencia é igual a {soma}')

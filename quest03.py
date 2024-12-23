cont = 1
numero = int(input("Digite um valor para ser calculado: "))

if numero < 0:
    print("O número deve ser maior do que zero")  
else:
    fatorial = 1

while cont <= numero:
    fatorial *= cont
    cont += 1

if numero > 0:
    print(f"O fatorial é: {fatorial}")




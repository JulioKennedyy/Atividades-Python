eprimo = []
naoprimo = []

def primo(n):
    if n < 2:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

numero = int(input("Digite o numero: "))
for i in range(numero+1):
    if primo(i):
        eprimo.append(i)
    else:
        naoprimo.append(i)

print(eprimo, naoprimo)
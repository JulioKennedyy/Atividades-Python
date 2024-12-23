N = int(input("Digite o valor de N: "))

lista_resultante = []

for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 == 0:
        lista_resultante.append("FizzBuzz")
    elif i % 3 == 0:
        lista_resultante.append("Fizz")
    elif i % 5 == 0:
        lista_resultante.append("Buzz")
    else:
        lista_resultante.append(i)


print(f"Lista resultante: {lista_resultante}")




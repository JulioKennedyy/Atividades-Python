#Peça ao usuário para digitar um nome completo e mostre:
#O nome todo em maiúsculas
#O nome todo em minúsculas
#Quantos caracteres tem o nome (sem espaços)

nome = str(input("Digite seu nome completo: "))
print(f"{nome.upper()} \n{nome.lower()}")
novafra = nome.replace((" "), (""))
print(len(novafra))

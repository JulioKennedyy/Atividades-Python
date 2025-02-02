#Crie uma função que receba uma string e retorne uma lista com todas as palavras em ordem inversa. Exemplo:
#Entrada: "Python é incrível" Saída: ["incrível", "é", "Python"]

frase = str(input("Digite a frase que vai ser invertida: "))
nova = frase.split(" ")
nova.reverse()
print(nova)

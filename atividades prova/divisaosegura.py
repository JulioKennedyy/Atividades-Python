#Escreva uma função chamada divisao_segura que receba dois números e retorne o resultado da divisão do primeiro pelo segundo. A função deve tratar a exceção de divisão por zero e, nesse caso, retornar a string "Divisão por zero não é permitida"

def divisao_segura(number1: float, number2: float):
    if number1 == 0 or number2 == 0:
        return("Divisão por zero não é permitida")
    else:
        return number1 / number2

print(divisao_segura(100, 2))
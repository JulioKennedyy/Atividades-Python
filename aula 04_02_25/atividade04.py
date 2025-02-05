#Faça um programa que receba o peso e a altura de um indivíduo e calcule seu imc através de uma função. 
#imc = Peso dividido pela altura ao quadrado.

def calcular_imc(peso: float, altura: float):
    resultado = peso / altura **2
    if resultado < 18.5:
        return (f"O seu resultado é {resultado} e está abaixo do peso")
    elif resultado >= 18.5 and resultado < 25.0:
        return (f"O seu resultado é {resultado} e está no peso normal")
    elif resultado >= 25.0 and resultado < 30.0:
        return (f"O seu resultado é {resultado} e está com sobrepeso")
    elif resultado >= 30.0 and resultado < 35.0:
        return (f"O seu resultado é {resultado} e está com obesidade grau 1")
    elif resultado >= 35.0 and resultado < 40.0:
        return (f"O seu resultado é {resultado} e está com obesidade grau 2")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
print(calcular_imc(peso, altura))
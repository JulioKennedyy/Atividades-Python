velocarro = int(input("Digite a velocidade do carro: "))
multa = 7
if velocarro > 80:
    print("Voce foi multado") 
    while velocarro ++1:
        a = (velocarro - 80) * multa 
        print("O valor da sua multa é: {}" .format(a))
        break
else: 
    print("De boa")
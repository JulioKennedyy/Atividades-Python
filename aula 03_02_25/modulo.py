import matematica as mt

while True:
    n1 = int(input("Digite o primeiro numero a ser calculado: "))
    n2 = int(input("Digite o segundo numero a ser calculado: "))
    ope = str(input("Digite a operação desejada (+,-,* ou /): "))

    match ope:
        case("+"):
            print(mt.soma(n1,n2))
        
        case("-"):
            print(mt.sub(n1,n2))
        
        case("*"):
            print(mt.multi(n1,n2))

        case("/"):
            print(mt.divi(n1,n2))
    
    sair = str(input("Digite x caso queira parar: ")).lower()
    if sair == "x":
        break
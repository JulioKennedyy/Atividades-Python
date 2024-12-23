"""a = int(input("Digite um valor: "))
b = int(input("Digite um outro valor: "))
som = a+b
dim = a-b
mul = a*b
div = a/b
print("Soma: {}".format(som),"Subtração: {}".format(dim),"Multiplicação: {}".format(mul),"Divisão: {}".format(div))"""

#abrindo um try para caso tenha erro no codigo e pedindo os valores ao usuario
try:
    nu1 = int(input("Digite um valor: "))
    nu2 = int(input("Digite um outro valor: "))
    ope = str(input("Digite a operação(+,-,*,/): "))

#comparação com cada operação aceita, caso não seja um valor ou número, caem no else e no except
    if ope == "+":
        print(nu1+nu2)
    elif ope == "-":
        print(nu1-nu2)
    elif ope == "*":
        print(nu1*nu2)
    elif ope == "/":
        print(nu1/nu2)
    else:
        print("Operação invalida")
except ValueError:
    print("Somente números")
    
"""ano = int(input("Digite um ano: "))
ano_divisivel_por_quatro = (ano % 4 == 0)
ano_divisivel_por_cem = (ano % 100==0)
ano_divisivel_por_400 = (ano % 400==0)
if ano_divisivel_por_quatro:
    if (not ano_divisivel_por_cem):
        if ano_divisivel_por_400:
            print("ano bissexto")
        else:
            print("Não é bissexto")
    else:
        print("É bissexto")    
else:
    print("Não é bissexto")"""
    
"""ano = int(input("Digite um ano: "))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print("Bissexto")
else:
    print("Não é bissexto")"""




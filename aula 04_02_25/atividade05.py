#Faça um programa que receba uma frase do usuário e informe quais letras e quantas vezes cada uma aparece na frase.

def achar_letra(frase: str):
    nova = frase.replace(" ", "")
    verificados = []
    for x in nova:
        if x not in verificados:
            verificados.append(x)
            quantidade = nova.count(x)
            print(f"A letra {x} aparece {quantidade} vezes")

frase = str(input("Digite sua frase: "))
print(achar_letra(frase))
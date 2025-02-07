def catch_vogais(palavra: str):
    for letra in palavra.lower():
        if letra in "aeiou":
            print(letra)

print(catch_vogais("Banana"))
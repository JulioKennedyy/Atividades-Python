dicionario = {
    "hi": "oi",
    "hello": "ola",
    "number": "numero",
    "i": "eu",
    "love": "amo",
    "you": "voce",
    "say": "dizer",
    "world": "mundo",
    "too": "tambem",
    "how": "como",
    "are": "estão",
    "good": "bom",
    "morning": "manhã",
    "night": "noite",
    "friend": "amigo",
    "this": "isso",
    "is": "é"
}

def traduzir(frase: str):
    palavras = frase.lower().split()  
    frase_traduzida = []

    for palavra in palavras:
        if palavra in dicionario:
            frase_traduzida.append(dicionario[palavra])
        else:
            frase_traduzida.append(palavra)
    return " ".join(frase_traduzida)

print(traduzir("you are my friend good night"))


def transferir(valor1,quanti, valor2):
    if valor1 < quanti:
        raise Exception("Valor passado é maior que o que esta na conta")
    else:
        valor2 += quanti
        valor1 -= quanti
        return (f"Seu saldo atual é {valor1} e foi passado {quanti}, {valor2}")
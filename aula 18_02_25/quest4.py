def buscar_palavra(lista,palavra):
    if palavra not in lista:
        print("Palavra não encontrada")
    else:
        return lista.index(palavra)
    try:
        if not isinstance(lista, list):
            raise ValueError("O valor não é uma lista")
    except Exception as ex:
        return("Erro", ex)

print(buscar_palavra(["arroz","Feijao"], "banana"))
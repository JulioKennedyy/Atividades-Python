lista1 = ["1", "2", "3", "10"]
lista2 = ["4", "5", "6", "5"]

def multiplicar_listas(lista1,lista2):
    nova = []
    try:
        if len(lista1) != len(lista2):
            raise Exception("Listas com tamanhos diferentes")
        for x, y in zip(lista1, lista2):
            
                x = int(x)
                y = int(y)
                nova.append(x*y)
    except ValueError:
        print("Listas incompativeis")
    except TypeError:
        print("Listas incompativeis")
    except Exception as ex:
        print("Erro", ex)
    else:
        return nova

print(multiplicar_listas(lista1, lista2))
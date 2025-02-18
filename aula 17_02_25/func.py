def verifi_idade(idade):
    try:
        idade2 = idade.split("/")
        idade2[0] = int(idade2[0])
        idade2[1] = int(idade2[1])
        idade2[2] = int(idade2[2])
        if idade2[0] > 31:
            raise Exception("Os dias vão somente ate o dia 31")
        if idade2[1] > 12:
            raise Exception("Os meses são apenas 12")
        if idade2[2] > 2025 and idade2[2] < 1910:
            raise Exception("ano invalido")
        if idade2[1] == "02" or idade2[1] == "2" and idade[2] > "29":
            raise Exception("fevereiro vai ate o dia 29")
    
        return 2025 - idade2[2]

    
    except ValueError:
        print("Somente numeros")
    except Exception as ex:
        print("Erro", ex)


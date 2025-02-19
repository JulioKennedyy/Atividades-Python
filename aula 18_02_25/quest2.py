def calculadora():
    try:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        while True:
            ope = str(input("Digite a operação(+, -, /, *): "))
            if ope not in ("+-/*"):
                print("Operação inválida")
                continue
            else:
                break
        match ope:
            case("+"):
               return a + b
            case("-"):
               return a - b
            case("/"):
               return a / b
            case("*"):
               return a * b
    
    except ValueError:
        print("Valor indefinido")
    except ZeroDivisionError:
        print("Não se pode dividir por zero")
    except Exception as ex:
        print("Erro", ex)

print(calculadora())
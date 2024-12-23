princ = []  
maio = meno = 0  

while True:
    nome = str(input("Digite seu nome: "))
    peso = float(input("Digite seu peso: "))
    princ.append([nome, peso])  
    
    sair = str(input("Quer sair? [S/N]: ")).strip().upper()
    if sair == "S":
        break

if princ:
    pesos = [p[1] for p in princ]  # Lista apenas com os pesos
    maio = max(pesos)
    meno = min(pesos)

print(f"Foram cadastradas {len(princ)} pessoas.")
print(f"O maior peso foi de {maio:.2f} kg. Peso de ", end="")
for p in princ:
    if p[1] == maio:
        print(f"[{p[0]}]", end=" ")
print()
print(f"O menor peso foi de {meno:.2f} kg. Peso de ", end="")
for p in princ:
    if p[1] == meno:
        print(f"[{p[0]}]", end=" ")
print()

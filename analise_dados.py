import pandas as pd

dados = [
    {"Nome":"Ana","Vendas":120},
    {"Nome":"Paulo","Vendas":150}
]

dd = pd.DataFrame(dados)
print(dd)
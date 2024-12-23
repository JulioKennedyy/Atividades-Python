numeros = [-15, -8, 0, 5, 12, 18, -3]

classificacao = ["Positivo" if num > 0 else "Zero" if num == 0 else "Negativo" if num < 0 else "Outro" for num in numeros ] 

par_ou_impar = ["Par" if num % 2 == 0 else "Impar" for num in numeros]  

categorias = [
            "Muito pequeno" if num < -10 else 
            "Pequeno" if num >= - 10 and num <= 0 else 
            "Médio" if num >= 1 and num <= 10 else 
            "Grande" 
            for num in numeros
]  

print("Classificação (Positivo/Negativo/Zero):", classificacao)
print("Classificação (Par/Ímpar):", par_ou_impar)
print("Categorias:", categorias)



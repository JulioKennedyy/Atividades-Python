num = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = num / num2
num4 = num % num2
x = num
while True:
    if num < num2:
     print("O primeiro número deve ser maior!")
     break
    x -= 1
    if x == num3:
       print(f"A divisão é igual a {x} e o resto é {num4}")
       break
    
    

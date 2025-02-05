#Faça um programa que receba do usuário a quantidade de caracteres e gere uma senha segura para o mesmo. O usuário também terá a opção de informar se quer a senha só com números, com números e letras ou números, letras e caracteres especiais. Para isso deve ser criada uma função chamada gerar_senha que se encontra em um módulos chamado utils/password.
#Utilizar do módulos string string.ascii_letters, para letras, string.digits para números e string.punctuation para caracteres especiais.
import utils.password as ps

while True:
    quanti_caracteres = int(input("Digite a quantidade de caracteres desejada: "))
    tipo_senha = int(input("Digite qual tipo de senha deseja \n (1) Senha numerica \n (2) Senha com palavras e numeros \n (3) Palavras e caracteres especiais \n : "))
    eu = ps.gerar_senha(tipo_senha,quanti_caracteres)
    print(eu)
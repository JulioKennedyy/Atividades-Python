import string as s
import random as r

def gerar_senha(tipo_senha: int, quanti_caracteres: int):
    match tipo_senha:
        case (1):
            random_number = ''.join(r.choices(s.digits, k=quanti_caracteres))
            return random_number
        case (2):
            random_string = ''.join(r.choices(s.ascii_letters, k=quanti_caracteres//2))  
            random_number = ''.join(r.choices(s.digits, k=quanti_caracteres//2))
            if quanti_caracteres % 2 == 1:
                new_element = ''.join(r.choices(s.ascii_letters, k=1))
                return new_element + random_string + random_number
            else:
                return random_string + random_number
        case (3):
            random_string = ''.join(r.choices(s.ascii_letters, k=quanti_caracteres//2))  
            random_special = ''.join(r.choices(s.punctuation, k=quanti_caracteres//2))
            if quanti_caracteres % 2 == 1:
                new_element = ''.join(r.choices(s.ascii_letters, k=1))
                return new_element + random_string + random_special
            else:
                return random_string + random_special

import random
import string

def generate_fake_apple_giftcard_code():
    code_length = 16
    prefix = "APL"  # Prefixo fictício para os códigos
    chars = string.ascii_uppercase + string.digits

    # Gera uma sequência aleatória de caracteres para completar o código
    random_chars = ''.join(random.choice(chars) for _ in range(code_length - len(prefix)))

    # Concatena o prefixo fictício com a sequência aleatória gerada
    code = prefix + random_chars
    return code

# Exemplo de uso:
giftcard_code = generate_fake_apple_giftcard_code()
print(giftcard_code)


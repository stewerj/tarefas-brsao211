import random
import string

def gerar_senha(tamanho=8):
    caracteres = string.ascii_letters + string.digits + "@!*#$%&"
    senha = ''
    for i in range(tamanho_senha):
        senha += random.choice(caracteres)
    return senha

tamanho = int(input("Digite o tamanho da senha: "))
senha = tamanho_senha(tamanho)

print(f"Senha: {senha}")
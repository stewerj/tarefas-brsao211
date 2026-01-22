import random
import string

<<<<<<< HEAD
def gerar_senha(tamanho_senha=8):
    caracteres = string.ascii_letters + string.digits + "@!*#$%&"
    senha = ''
    for i in range(tamanho_senha):
        senha += random.choice(caracteres)
=======
def gerar_senha(tamanho_senha):
    caracteres = string. ascii_letters + string.digits+"@#$%¨&*"
    senha = ''
    
    for i in range (tamanho_senha):
        senha += random.choice(caracteres)

>>>>>>> 84d2ae6b006d356d80063c1e10ead6a509090290
    return senha

tamanho = int(input("Digite o tamanho da senha: "))
senha = gerar_senha(tamanho)
<<<<<<< HEAD

print(f"Senha: {senha}")
=======
print(f"Senha: {senha}")    
>>>>>>> 84d2ae6b006d356d80063c1e10ead6a509090290

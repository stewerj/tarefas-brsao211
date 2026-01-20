import requests

def obter_ususario_aleatorio():
    url = "https://randomuser.me/api/"
    try:
        requests = requests.get(url)
        dados = requests.json()

        nome = f" {dados["name"]["first"]} {dados["name"]["last"]}"
        email = dados["email"]
        pais = dados["location"]["country"]
        sobrenome = dados["name"]["last"]

        return f"nome: {nome}, email: {email}, pais: {pais}, "
    
    except requests.RequestException as e:
    return f"Erro ao obter usuário aleatorio: {e}"

usuario = obter_ususario_aleatorio()
print(usuario) 
 
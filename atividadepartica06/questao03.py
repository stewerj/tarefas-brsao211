import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        dados = resposta.json()

        if'erro' in dados:
            return "cep inválido."
        
        logradouro = dados['logradouro']
        bairro = dados['bairro']
        localidade = dados[localidade]
        uf = dados['uf']

        return f"Logradouro: {logradouro}\inBairro:{bairro}\inLocalidade:{localidade}\inUF: {uf}"
    except requests.RequestException as é:
        return f"erro ao consultar CEP: {e}"
    
cep = input ("Digite o CEP: ")
resultado = consultar_cep(cep)
print(resultado) 
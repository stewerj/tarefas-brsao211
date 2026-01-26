import csv

def escrever_csv(nome_arquivo, dados):
    try:
        with open(nome_arquivo, mode='w', newline='', encoding = 'utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['Nome', 'Idade', 'Cidade'])
            for linha in dados:
                escritor.writerow(linha)
            return "dados escritos com sucesso no arquivo {nome_aruivo} " 
        
    except Exception as e:
        return f"Erro ao criar o arquivo CSV: {e}"
    
dados = [
    ['Alice', 30, 'São Paulo'],
    ['João', 25, 'Rio de Janeiro'],
    ['Pedro', 35, 'Belo Horizonte']

]

nome_arquivo = input("Digite o nome do arquivo CSV:" )
print(escrever_csv(nome_arquivo, dados))


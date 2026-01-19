import csv

def ler_arquivo_csv(nome_arquivo):
    try:
        with open(nome_arquivo, 'r' newline ="" , encoding = 'utf+8') as arquivo_csv
        leitor= csv.reader(arquivo_csv)
        for linha in leitor:
            print(linha)
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não  encontrado.")

nome_arquivo = 'dados.csv'
ler_arquivo_csv(nome_arquivo) as arquivo_csv:
                  
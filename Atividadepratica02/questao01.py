valor_reais = float(input("Digite o valor em reais: "))
cotacao_dolar = 5.37
cotacao_euros = 6.25

valor_dolar = valor_reais / cotacao_dolar

valor_euros = valor_reais / cotacao_euros

print(f"Valor em Reais: R${valor_reais:.2f}")

print(f"Valor em Dólares: ${valor_dolar:.2f}")

print(f"Valor em Euros: €{valor_euros:.2f}")

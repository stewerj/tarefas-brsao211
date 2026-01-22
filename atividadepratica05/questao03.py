def calcular_desconto (valor_produto, porcentagem_desconto):
    desconto = valor_produto * (porcentagem_desconto / 100)
    valor_final = valor_produto - desconto
    return valor_final

    
    

valor = float (input ("Digite o valor do produto: " )) 
porcentagem = float (input ("Digite a porcentagem de desconto: " ))

desconto = calcular_desconto(valor, porcentagem)
<<<<<<< HEAD

print (f"O valor com desconto é : R$ {desconto:.2f}")
=======
print (f"O valor final do produto é : R$ {desconto:.2f}")
>>>>>>> 84d2ae6b006d356d80063c1e10ead6a509090290

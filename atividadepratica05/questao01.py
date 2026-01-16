def calcular_gorjeta (valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100) 
    return gorjeta
    

valor_conta = float (input ("Digite o valor da conta:" )) 
percentual_gorjeta = float (input ("Digite o percentual da gorjeta:" ))

gorgeta = calcular_gorjeta (valor_conta, percentual_gorjeta)

print (f"O valor da gorjeta é: R$ {gorgeta:.2f}")

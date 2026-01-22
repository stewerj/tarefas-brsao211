pares = 0
impares = 0

while True:
    try:
        entrada = input("Digite um número ou 'fim' para sair:")

        if entrada.lower() == 'fim':
            break

        numero = int(entrada)
    
        if numero % 2 == 0:
            pares += 1
            print (f"O número {numero} é par.")
            pares += 1

        else:
            impares += 1
            print (f"O número {numero} é ímpar.")
            impares += 1

    except ValueError:
        print("Você deve digitar apenas números.")

print (f"Números pares: {pares}")
print (f"Números ímpares: {impares}")


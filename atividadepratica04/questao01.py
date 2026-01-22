while True:
    try:
        numero1 = float(input("Digite o primeiro numero: "))
        numero2 = float(input("Digite o segundo numero: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = numero1 + numero2
        
        elif operacao == '-':
            resultado = numero1 - numero2

        elif operacao == '*':
            resultado = numero1 * numero2

        elif operacao == '/':
            resultado = numero1 / numero2
        else:
            raise Exception()
        
        print(f"O resultado é: {resultado}")
        break

    except ValueError:
        print("Você deve digitar apenas números.")
    except ZeroDivisionError:
        print("Não é possível dividir por zero.")
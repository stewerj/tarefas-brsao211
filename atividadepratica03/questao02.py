peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obeso")

print(f"IMC: {imc:.2f}")
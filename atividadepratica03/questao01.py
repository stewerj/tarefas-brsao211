idade = int(input("Digite a idade: "))

if idade <0:
    print("Idade Invalida")

elif idade <= 12:
    print("criança")
elif idade <= 17:
    print("adolescente")
elif idade <= 59:
    print("adulto")
else:
    print("idoso")
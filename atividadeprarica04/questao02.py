notas = []

while True:
    try:
        entrada = input("Digite uma nota entre 0 e 10 (ou 'fim'para sair): ")
        nota = float(input("Digite uma nota entre 0 e 10 (ou -1 para finalizar): "))

        if entrada.lower() == 'fim':
            break
        nota = float(entrada)

        if nota == < 0 or nota > 10':
            raise Exception()
        nota.append(nota)

    except ValueError:
        print("Você deve digitar apenas números.")
    except Exception:
        print("Nota inválida.")
        
soma = 0

for nota in notas:
    soma += nota
media = soma / len(notas) 
print(f"Média final: {media:.2f}")
notas = []

while True:
   try:
      entrada = input("Digite uma nota entre 0 e 10 (ou 'fim' para sair): ")

      if entrada.lower() == 'fim':
         break
      
      nota = float(entrada)

      if nota < 0 or nota > 10:
         raise Exception ()
      
      notas.append(nota)
<<<<<<< HEAD:atividadeprarica04/questao02.py
      

   except ValueError:
        print("Você deve digitar apenas números.")
   except Exception:
        print("Nota inválida.")

soma = 0
for nota in notas:
    soma += nota

media = soma / len(notas)
print(len(notas))

print(f"Média final: {media:.2f}")
=======
   
   except ValueError:
        print("Você deve digitar apenas números.")
   except Exception:
        print("Nota invalida.")
soma = 0

for nota in notas:
   soma += nota

media = soma / len(notas)

print(len(notas))

print(f"Média final: {media:.2f}")

   
>>>>>>> 84d2ae6b006d356d80063c1e10ead6a509090290:atividadepratica04/questao02.py

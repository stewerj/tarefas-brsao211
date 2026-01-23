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
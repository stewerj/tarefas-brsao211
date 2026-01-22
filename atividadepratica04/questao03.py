while True:
    try:
        senha = input("Digite a senha: ")

        if senha.lower ()== "sair":
            print("Saindo do programa....")
            break


        if len(senha) < 8:
            raise Exception ("Senha deve ter pelo menos 8 caracteres.")
        
        tem_numero = False
        for caractere in senha:
            if caractere.isdigit():
                tem_numero = True
                break
<<<<<<< HEAD:atividadeprarica04/questao03.py
            if caractere in '0123456789':
=======
            if caractere in ("0123456789"):
>>>>>>> 84d2ae6b006d356d80063c1e10ead6a509090290:atividadepratica04/questao03.py
                tem_numero = True
                break

        if tem_numero == False:
            raise Exception ("Senha deve conter pelo menos um número.")
        print("Senha válida.")
        break

    except Exception as e:
        print(f"erro: {e} Tente Novamente!")
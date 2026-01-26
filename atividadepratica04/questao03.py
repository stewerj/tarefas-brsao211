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


            if caractere in ("0123456789"):

                tem_numero = True
            
                break

        if tem_numero == False:
            raise Exception ("Senha deve conter pelo menos um número.")
        print("Senha válida.")
        break

    except Exception as e:
        print(f"erro: {e} Tente Novamente!")
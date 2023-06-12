try:
    import os
    # Utilizado para dar um tempo ao mostrar informações antes de voltar ao menu_cadastro_login.
    import time
    from controladores import localizacao

    def limpar_tela():
        # Se for em um dispositivo linux, usa o clear, caso não, usa cls.
        os.system('cls' if os.name == 'nt' else 'clear')

    def cabecalho(escolha):
        limpar_tela()
        print("{:-^35}".format(f" Tela {escolha} "))
        print()

    def registrar():
        try:
            # Tenta abrir o arquivo, se não existir, cria um novo.
            open('./dados/armazenamento_cadastros.txt', 'a').close()
            cabecalho("Registrar")
            usuario = input("Digite o nome do usuário: ")
            senha = input("Digite a senha: ")

            # Checa se ja existe alguem com esse nome cadastrado.
            with open('./dados/armazenamento_cadastros.txt', 'r') as arquivo:
                usuarios = arquivo.readlines()

                if (usuario.strip() == '') or (senha.strip() == ''):
                    print("Você precisa digitar um nome de usuário e uma senha.")
                    time.sleep(2)
                    return False
                carcacteres_proibidos = ["|", " ", "\\"]

                # Checa se o nome de usuário ou a senha contém caracteres especiais que podem causar problemas ao serem usados.
                if any(caracter in usuario for caracter in carcacteres_proibidos) or any(caracter in senha for caracter in carcacteres_proibidos):
                    print("A sua senha ou nome de usuário não pode conter espaços, barras ou o caractere '|'.")
                    time.sleep(2)
                    return False
                
                if usuario == "VISITANTE":
                    print("Este nome de usuário não está disponível.")
                    time.sleep(2)
                    return False
                
                for usuarioCadastrado in usuarios:
                    arquivo_usuario = usuarioCadastrado.strip().split('|')[0]
                    if usuario == arquivo_usuario:
                        print("Esse nome de usúario já foi utilizado.")
                        time.sleep(2)
                        return False

            # Cadastra o usuário separando por '|' para ajudar na manipulação.
            with open('./dados/armazenamento_cadastros.txt', 'a') as cd:
                cd.write(usuario + '|' + senha + '\n')
            print("\nCadastro realizado com sucesso.")
            time.sleep(2)
            return True, usuario
        except IOError or FileNotFoundError:
            print("Erro para abrir arquivo.")
            time.sleep(2)
            return False

    def login():
        cabecalho("Login")
        usuario = input("Digite o nome do usuário: ")
        senha = input("Digite a senha: ")

        try:
            with open('./dados/armazenamento_cadastros.txt', 'r') as cd:
                usuarios = cd.readlines()
        except FileNotFoundError:
            print("Você precisa se registrar primeiro.")
            time.sleep(2)
            return False

        for usuarioCadastro in usuarios:
            # Checa se o usuário e a senha inseridos são correspondentes ao do cadastrado.
            cd_usuario, cd_senha = usuarioCadastro.replace(
                "\n", "").strip().split('|')
            try:

                if cd_usuario == usuario and cd_senha == senha:
                    cabecalho("Login")
                    print("Você está logado!")
                    time.sleep(2)
                    return True, usuario
            except:
                print("Falha ao realizar login.")
                continue
        cabecalho("Login")
        print("Usuário ou senha inválido.")
        time.sleep(2)
        return False, None


    def menu_cadastro_login():
        while True:
            cabecalho("Menu Principal ")
            print("1. Cadastrar-se\n")
            print("2. Continuar sem cadastro\n")
            print("3. Entrar\n")
            print("4. Sair\n")
            print("-" * 35)
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                logado, usuario_atual = registrar()
                if logado:
                    return usuario_atual
                else:
                    continue
            elif opcao == '2':
                return "VISITANTE"
            elif opcao == '3':
                logado, usuario_atual = login()
                if logado:
                    return usuario_atual  # Retorna o nome do usuário logado para usar no futuro
                else:
                    continue  # Se o usuário não for logado, volta para o menu_cadastro_login
            elif opcao == '4':
                limpar_tela()
                print("Saindo...")
                time.sleep(2)
                return '\sair_programa'
            else:
                limpar_tela()
                print("Opção inválida.")
                time.sleep(2)
except ModuleNotFoundError:
    print("A instalação não foi concluida corretamente.")

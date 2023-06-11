import os
# Utilizado para dar um tempo ao mostrar informações antes de voltar ao menu_cadastro_login.
import time
import localizacao

def limpar_tela():
    # Se for em um dispositivo Ios, usa o clear, caso não, usa cls.
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho(escolha):
    limpar_tela()
    print("{:-^35}".format(f" Tela {escolha} "))
    print()

def registrar():
    try:
        # Tenta abrir o arquivo, se não existir, cria um novo.
        open('armazenamento_cadastros.txt', 'a').close()

        cabecalho("Registrar")
        usuario = input("Digite o nome do usuário: ")
        senha = input("Digite a senha: ")

        # Checa se ja existe alguem com esse nome cadastrado.
        with open('armazenamento_cadastros.txt', 'r') as arquivo:
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
        with open('armazenamento_cadastros.txt', 'a') as cd:
            cd.write(usuario + '|' + senha + '\n')
        print("Cadastro realizado com sucesso.")
        return True, usuario
        time.sleep(2)
    except IOError:
        print("Erro ao tentar registrar o usuário.")
        time.sleep(2)

def login():
    cabecalho("Login")
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")

    try:
        with open('armazenamento_cadastros.txt', 'r') as cd:
            usuarios = cd.readlines()
    except FileNotFoundError:
        print("Você precisa se registrar primeiro.")
        time.sleep(2)
        return False

    for usuarioCadastro in usuarios:
        # Checa se o usuário e a senha inseridos são correspondentes ao do cadastrado.
        cd_usuario, cd_senha = usuarioCadastro.replace(
            "\n", "").strip().split('|')

        if cd_usuario == usuario and cd_senha == senha:
            cabecalho("Login")
            print("Você está logado!")
            time.sleep(2)
            return True, usuario

    cabecalho("Login")
    print("Usuário ou senha inválido.")
    time.sleep(2)
    return False


def menu_cadastro_login():
    while True:
        cabecalho("Menu Principal ")
        print("1. Cadastrar-se")
        print("2. Continuar sem cadastro")
        print()
        print("3. Entrar")
        print()
        print("4. Sair")
        print()
        print("-" * 35)
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            registrar()
        elif opcao == '2':
            return True
        elif opcao == '3':
            logado, usuario_atual = login()
            if logado:
                return usuario_atual  # Retorna o nome do usuário logado para usar no futuro
            else:
                pass  # Se o usuário não for logado, volta para o menu_cadastro_login
        elif opcao == '4':
            limpar_tela()
            print("Saindo...")
            time.sleep(2)
            return 'sair_programa'
        else:
            limpar_tela()
            print("Opção inválida.")
            time.sleep(2)



usuario_atual = menu_cadastro_login()
limpar_tela()

permissao = localizacao.verificar_permissao_localizacao(usuario_atual)

if not permissao:  # Se o usario atual não tiver permitido o acesso a localização a função irá perguntar se ele deseja.
    localizacao.pedir_permissao_localizacao(usuario_atual)

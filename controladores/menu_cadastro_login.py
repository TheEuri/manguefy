import os
import time  #Utilizado para dar um tempo ao mostrar informações antes de voltar ao menu_cadastro_login.

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')   #Se for em um dispositivo Ios, usa o clear, caso não, usa cls.


def cabecalho(escolha):
    limpar_tela()
    print("{:-^35}".format(f" Tela {escolha} "))
    print()

def registrar():
    try:
        #Tenta abrir o arquivo, se não existir, cria um novo.
        open('armazenamento_cadastros.txt', 'a').close()
        
        cabecalho("Registrar")
        usuario = input("Digite o nome do usuário: ")
        senha = input("Digite a senha: ")

        with open('armazenamento_cadastros.txt', 'r') as arquivo: #Checa se ja existe alguem com esse nome cadastrado.
            usuarios = arquivo.readlines()
            for usuarioCadastrado in usuarios:
                arquivo_usuario, arquivo_senha = usuarioCadastrado.strip().split('|')
                if usuario == arquivo_usuario:
                    print("Esse nome de usúario já foi utilizado.")
                    time.sleep(2)
                    return
                
        with open('armazenamento_cadastros.txt', 'a') as cd: #Cadastra o usuário separando por '|' para ajudar na manipulação. 
            cd.write(usuario + '|' + senha + '\n')
        print("Usuário cadastrado.")
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
        cd_usuario, cd_senha = usuarioCadastro.strip().split('|') #Checa se o usuário e a senha inseridos são correspondentes ao do cadastrado.

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
                return usuario_atual #Retorna o nome do usuário logado para usar no futuro
            else:
                pass #Se o usuário não for logado, volta para o menu_cadastro_login
        elif opcao == '4':
            limpar_tela()
            print("Saindo...")
            time.sleep(2)
            break
        else:
            limpar_tela()
            print("Opção inválida.")
            time.sleep(2)

def verificar_permisao_localizacao(usuario):
    open(f'{usuario}_localizacao.txt', 'a').close() #Tenta abrir o arquivo, se não existir, cria um novo.

    with open(f"{usuario}_localizacao.txt", 'r') as arquivo:
        localizacao = arquivo.read()
        arquivo.close()
        if localizacao == '1': #Checa se o usuário atual permitiu a localização.
            return True
        else:
            return False
  
def pedir_permissao_localizacao(usuario):
    with open(f"{usuario}_localizacao.txt", 'w') as arquivo:
        escolha = input("Deseja permitir o acesso a sua localização? (S/N): ").lower()
        if escolha.lower() == 's':
            arquivo.write('1')
        else:
            limpar_tela()
            print("Texto explicando que o acesso a localização é necessário para o funcionamento do programa.")
            escolha = input("Você tem certeza que deseja continuar sem permitir o acesso? (S/N)").lower()
            if escolha == 's':
                arquivo.write('0')
            else:
                pedir_permissao_localizacao(usuario)

usuario_atual = menu_cadastro_login()
limpar_tela()

permissao = verificar_permisao_localizacao(usuario_atual)

if not permissao:  #Se o usario atual não tiver permitido o acesso a localização a função irá perguntar se ele deseja.
    pedir_permissao_localizacao(usuario_atual)




  

import os
import time
import geocoder

def inicio():
    print("Seja bem vindo ao MANGUEFY")
    time.sleep(2)
    os.system("cls")
    print("O Manguefy é um aplicativo projetado para você conhecer mais da cultura recifense e do\nManguebeat, movimento cultural extremamente significativo.\nAqui você vai poder fazer rotas interativas e ter acesso a mídias que se conectam por meio da geolocalização com a rota que você estiver fazendo.\nOs áudios disponibilizados têm relação direta com os locais que você estiver, tornando a experiência de conhecer a cultura mais dinámica e acessível no dia a dia.")
    avanc=input("Avançar? ").lower
    if avanc==("sim"):
        return

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def local():
    global lat, lng
    os.system("cls")
    print("Entenda melhor a nossa proposta: ")
    print("explicação")
    ask=input("Você autoriza o uso? ").lower
    if ask==("sim"):
        g = geocoder.ip('me')
        if g.ok:
            lat, lng = g.latlng
        else:
            print("Falha ao se conectar ao servidor")
    else:
        print("Para usar o nosso app será necessário autorizar a localização \nnas configurações depois.")

def registrar():
    limparTela()
    print("{:-^35}".format(" Tela de registro "))
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")

    try:
        with open('armazenamento_cadastros.txt', 'a') as cd:
            cd.write(usuario + '|' + senha + '\n')
        print("Usuário cadastrado.")
    except IOError:
        print("Erro ao tentar registrar o usuário.")

    time.sleep(2)

def login():
    limparTela()
    print("{:-^35}".format(" Tela de login "))
    usuario_input = input("Digite o nome do usuário: ")
    senha_input = input("Digite a senha: ")

    try:
        with open('armazenamento_cadastros.txt', 'r') as cd:
            usuarios = cd.readlines()
    except FileNotFoundError:
        print("Você precisa se registrar primeiro.")
        time.sleep(2)
        return False

    for usuario in usuarios:
        cd_usuario, cd_senha = usuario.strip().split('|')

        if cd_usuario == usuario_input and cd_senha == senha_input:
            limparTela()
            print("{:-^35}".format(" Tela de login "))
            print("Você está logado!")
            time.sleep(2)
            return True
    limparTela()
    print("{:-^35}".format(" Tela de login "))
    print("Usuário ou senha inválido.")
    time.sleep(2)
    return False

def menu():
    while True:
        limparTela()
        print("{:-^35}".format(" Menu principal "))
        print()
        print("1. Registrar")
        print("2. Login")
        print()
        print("3. Sair")
        print()
        print("-" * 35)
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            registrar()
        elif opcao == '2':
            login()
        elif opcao == '3':
            print("Saindo...")
            time.sleep(2)
            break
        else:
            print("Opção inválida.")
            time.sleep(2)
inicio()
menu()

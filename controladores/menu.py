import os
import time  #utilizado para dar um tempo ao mostrar informações antes de voltar ao menu

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')   #se for em um dispositivo Ios, usa o clear, caso não, usa cls

def cabecalho():
    limparTela()
    print("{:-^35}".format(" Tela De Login "))

def registrar():
    cabecalho()
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
    cabecalho()
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")

    try:
        with open('armazenamento_cadastros.txt', 'r') as cd:
            usuario = cd.readlines()
    except FileNotFoundError:
        print("Você precisa se registrar primeiro.")
        time.sleep(2)
        return False

    for usuario in usuario:
        cd_usuario, cd_senha = usuario.strip().split('|')

        if cd_usuario == usuario and cd_senha == senha:
            cabecalho()
            print("Você está logado!")
            time.sleep(2)
            return True

    cabecalho()
    print("Usuário ou senha inválido.")
    time.sleep(2)
    return False

def menu():
    while True:
        cabecalho()
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

menu()

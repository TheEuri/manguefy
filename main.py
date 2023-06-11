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
    global usuario_input
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

def conta():
    os.system("cls")
    print(usuario_input)
    print("E-mail e telefone")
    print("Cnfigurações")
    print("Historico de rotas")
    print("Rotas favoritas")

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
import os
from colorama import init, Fore, Style

init()
os.system("cls")

def informacoes():
    w = " "
    while w != "x":
        print("-" * 10, "Sobre o propósito", "-" * 10)
        print("O Manguefy tem como grande objetivo disseminar\ncultura e turismo por meio do Manguebeat.\nProcurando democratizar o conhecimento e\nacesso a cultura para a população.")

        print("-" * 10, "Funcionamento do aplicativo", "-" * 10)
        print("Por meio da geolocalização o app sugere rotas\ne faz uma curadoria\n ")

        print("Pergunta frequente")
        print("1. Como escolho rotas definidas?")
        print("2. Voltar")
        entrada = input("Digite o número para onde você deseja continuar: ")
        
        try:
            if int(entrada) == 1:
                os.system("cls")
                print("Após clicar em 'Rota definida', você terá\nacesso às opções de rotas. É só escolher a que desejar e\niniciar o seu passeio.")
        except ValueError:
            continue
        
        if int(entrada) == 2:
            os.system("cls")
            w = 'x'


def passeio():
    os.system("clear")
    print("Qual será a forma de passeio?")
    print("1 - A pé")
    print("2 - De carro")
    print("3 - De de bicicleta")
    opcao = int(input("Qual a sua opção? "))
    if opcao == 1:
        print("Você escolheu a opção 1 - A pé")
    elif opcao == 2:
        print("Você escolheu a opção 2 - De carro")
    elif opcao == 3:
        print("Você escolheu a opção 3 - De bicicleta")
    elif opcao == 4:
        #return opcao anterior
        print() 
    else:
        print("Opção inválida!")
    print ("fazer um passeio \n Como você quer seguir sua rota?")
    print("1 - Rota definida")
    print("2 - Rota personalizada")
    opcao1 = int(input("Qual a sua opção? "))
    if opcao1 == 1:
        print("1 - Rota Manguebeat\n 2 - Rota Artesanato\n 3 - Rota dos Poetas\n 4 - Rota do Carnaval\n 5 - Rota do Praieira\n 6 - Rota da Lama ao Caos")
        sair = input("Sair")
        if sair == "sair":
            print()
            #return opcao anterior
    buscar = []
    if opcao1 == 2:
        while True:
            concluir = input("Concluir")
            if concluir == "concluir":
                buscando = int(input("Buscar"))
                buscando.append(buscar)
                print("Localização Salva", buscar)
                tirar = input("Tirar localização")
                if tirar == "sim" or "Sim":
                    palavra = buscando
                    buscando.remove(palavra)
                else:
                    print()
            elif concluir == "sair":
                print("saindo")
                #return opcao anterior or BREAK!!! 
            Localização = input("Sua localização")
            if Localização == True:
                print()
                #return opcao anterior (ESSE LOCALIZAÇÃO SERVE COMO GPS DO GOOGLE PARA FACILITAR A LOCALIZAÇÃO ATUAL // SEM FUÇÃO ATUAL)
            cont = input('concluir Seleção?')
            if cont == 'sim':
                print()
                break
            else:
                print('continuando a adicionar...')

def telacommapa():
    ask=input("Informações, conta ou Fazer um passeio? ").lower
    if ask == ("informações"):
        informacoes()
    if ask == ("conta"):
        conta()
    if ask == ("passeio"):
        informacoes()




inicio()
menu()




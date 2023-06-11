import os
from time import sleep


def limpar_tela():
    # Se for em um dispositivo linux, usa o clear, caso não, usa cls.
    os.system('cls' if os.name == 'nt' else 'clear')


def boasvindas():
    # Mostra o logo do programa
    with open('./misc/manguefy-logo.txt', 'r') as logo:
        limpar_tela()
        print(logo.read())
        print("Seja bem vindo(a) ao Manguefy!")
        print("\nIniciando....")
        sleep(2)
        limpar_tela()

    print('-' * 50, 'Sobre o Manguefy', '-' * 50)
    print('O Manguefy é um aplicativo projetado para você conhecer mais da cultura recifense e do Manguebeat, \nmovimento cultural extremamente significativo. Aqui você vai poder fazer rotas interativas e ter acesso a \nmídias que se conectam por meio da geolocalização com a rota que você estiver fazendo. Os áudios disponibilizados \ntêm relação direta com os locais que você estiver, tornando a experiência de conhecer a cultura mais \ndinâmica e acessível no dia a dia.')
    print('-'*118)
    input("\nPressione ENTER para continuar")


def informacoes():
    w = " "
    while w != "x":
        limpar_tela()
        print("-" * 15, "Sobre o propósito", "-" * 15)
        print("O Manguefy tem como grande objetivo disseminar\ncultura e turismo por meio do Manguebeat.\nProcurando democratizar o conhecimento e\nacesso a cultura para a população.\n")

        print("-" * 10, "Funcionamento do aplicativo", "-" * 10)
        print("Por meio da geolocalização o app sugere rotas\ne faz uma curadoria\n")

        print("-" * 15, "Perguntas frequentes", "-" * 15)
        print("1. Como escolho rotas definidas?")
        print("2. Voltar")
        entrada = input("\nEscolha uma opção: ")

        try:
            if int(entrada) == 1:
                limpar_tela()
                print("Após clicar em 'Rota definida', você terá\nacesso às opções de rotas. É só escolher a que desejar e\niniciar o seu passeio.")
                input("\nPressione ENTER para voltar ao menu de informações")
        except ValueError:
            continue

        if int(entrada) == 2:
            limpar_tela()
            w = 'x'

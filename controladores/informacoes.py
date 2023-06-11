import os

def limpar_tela():
    # Se for em um dispositivo Ios, usa o clear, caso não, usa cls.
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()

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
                limpar_tela()
                print("Após clicar em 'Rota definida', você terá\nacesso às opções de rotas. É só escolher a que desejar e\niniciar o seu passeio.")
        except ValueError:
            continue
        
        if int(entrada) == 2:
            limpar_tela()
            w = 'x'
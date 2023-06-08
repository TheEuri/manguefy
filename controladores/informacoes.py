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

informacoes()

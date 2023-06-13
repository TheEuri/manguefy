import os
from time import sleep
from controladores.sobre import informacoes
from controladores.iniciar_passeio import iniciar_passeio

def limpar_tela():
    # Se for em um dispositivo linux, usa o clear, caso não, usa cls.
    os.system('cls' if os.name == 'nt' else 'clear')

def ver_conta(usuario):
    limpar_tela()
    if usuario=="VISITANTE":
       print("Você ainda não esta cadastrado")
    else:
        print(f"Seu usuário: {usuario}")
    print("{E-mail ou telefone}\n")
    print("Configurações")
    print("Historico de rotas")
    print("Rotas favoritas\n")
    input("Pressione ENTER para voltar ao menu principal\n")

def menu_principal(usuario):
    while True:
      limpar_tela()
      print(f"Logado como {usuario}\n")
      print("-" * 15, "Qual você deseja?", "-" * 15)
      print("\n1. Ver conta\n")
      print("2. Ver central de informações e ajuda\n")
      print("3. Fazer um passeio\n")
      print("4. Sair\n")
      print('-'*49)
      opcao = input("\nEscolha uma opção: ")

      if opcao == '1':
        ver_conta(usuario)
      elif opcao == '2':
         informacoes()
      elif opcao == '3':
         iniciar_passeio(usuario)
      elif opcao == '4':
          break
      else:
          print("Opção inválida, tente novamente.")
          sleep(2)

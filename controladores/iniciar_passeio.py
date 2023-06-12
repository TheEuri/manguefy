from time import sleep
import os
from dotenv import load_dotenv
import googlemaps
import folium
import polyline
from datetime import datetime

load_dotenv()
print(os.environ.get('GOOGLE_API_KEY'))

gmaps = googlemaps.Client(key=os.environ.get('GOOGLE_API_KEY'))




rotas = {
    '1': {
      'nome': 'Manguebeat',
      'pontos': [],
      'quilometragem': 10
    },
    '2': {
      'nome': 'Artesanato',
      'pontos': [],
      'quilometragem': 15
    },
    '3': {
      'nome': 'dos Poetas',
      'pontos': [],
      'quilometragem': 5
    },
    '4': {
      'nome': 'do carnaval',
      'pontos': [],
      'quilometragem': 20
    },
    '5': {
      'nome': 'Praiera',
      'pontos': [],
      'quilometragem': 18
    },
    '6': {
      'nome': 'da lama ao caos',
      'pontos': [],
      'quilometragem': 8
    }
  }

def limpar_tela():
    # Se for em um dispositivo linux, usa o clear, caso não, usa cls.
    os.system('cls' if os.name == 'nt' else 'clear')

def modo_locomocao():
    while True:
      limpar_tela()
      print('-'*15, 'Qual será seu modo de locomoção?', '-'*15)
      print('\n1 - A pé')
      print('\n2 - De carro')
      print('\n3 - De bicicleta')
      print('\n4 - Voltar\n')
      print('-'*60)
      opcao = input("\nEscolha uma opção: ")

      limpar_tela()
      if opcao == '1':
        print('\nVocê escolheu a opção 1 - A pé\n')
        confirma = input('\nDigite S para confirmar ou N para cancelar: ').lower()
        if confirma == 's':
          print('\nModo de locomoção definido como a pé\n')
          sleep(2)
          return 1
        else:
          print('\nVoltando para o menu...\n')
          sleep(2)
          continue
      elif opcao == '2':
        print('\nVocê escolheu a opção 2 - De carro\n')
        confirma = input('\nDigite S para confirmar ou N para cancelar: ').lower()
        if confirma == 's':
          print('\nModo de locomoção definido como de carro\n')
          sleep(2)
          return 2
        else:
          print('\nVoltando para o menu...\n')
          sleep(2)
          continue
      elif opcao == '3':
        print('\nVocê escolheu a opção 3 - De bicicleta\n')
        confirma = input('\nDigite S para confirmar ou N para cancelar: ').lower()
        if confirma == 's':
          print('\nModo de locomoção definido como de bicicleta\n')
          sleep(2)
          return 3
        else:
          print('\nVoltando para o menu...\n')
          sleep(2)
          continue
      elif opcao == '4':
        print('\nVoltando para o menu...\n')
        sleep(2)
        return False

def escolher_tipo_rota():
  while True:
    limpar_tela()
    print('-'*15, 'Escolha o tipo de rota', '-'*15)
    print('\n1 - Rota definida')
    print('\n2 - Rota personalizada')
    print('\n3 - Voltar\n')
    print('-'*60)
    opcao = input("\nEscolha uma opção: ")

    limpar_tela()
    if opcao == '1':
      print('\nVocê escolheu a opção 1 - Rota definida\n')
      confirma = input('\nDigite S para confirmar ou N para cancelar: ').lower()
      if confirma == 's':
        print('\nVocê escolheu rota definida.\n')
        sleep(2)
        return 1
      else:
        print('\nVoltando para o menu...\n')
        sleep(2)
        continue
    elif opcao == '2':
      print('\nVocê escolheu a opção 2 - Rota personalizada\n')
      confirma = input('\nDigite S para confirmar ou N para cancelar: ').lower()
      if confirma == 's':
        print('\nVocê escolheu rota personalizada.\n')
        sleep(2)
        return 2
      else:
        print('\nVoltando para o menu...\n')
        sleep(2)
        continue
    elif opcao == '3':
      print('\nVoltando para o menu...\n')
      sleep(2)
      return False
    
def selecionar_rota():
  while True:
    limpar_tela()
    print('-'*15, 'Escolha uma rota', '-'*15)
    for rota in rotas:
      print(f'{rota} - Rota {rotas[rota]["nome"]} ({rotas[rota]["quilometragem"]}km)')
    print('\n7 - Voltar\n')
    print('-'*60)
    opcao = input("\nEscolha uma opção: ")

    limpar_tela()
    opcao_valida = False
    for rota in rotas:
      if opcao == rota:
        opcao_valida = True
        print(f'\nVocê escolheu a opção {rota} - Rota {rotas[rota]["nome"]} ({rotas[rota]["quilometragem"]}km)\n')
        confirma = input('\nDigite S para confirmar ou N para cancelar: ').lower()
        if confirma == 's':
          print(f'\nVocê escolheu a rota {rota} - Rota {rotas[rota]["nome"]} ({rotas[rota]["quilometragem"]}km)\n')
          sleep(2)
          return rota
        else:
          print('\nVoltando para o menu...\n')
          sleep(2)
          continue
    if opcao == '7':
      print('\nVoltando para o menu...\n')
      sleep(2)
      return False
    if opcao_valida == False:
      print('\nOpção inválida, tente novamente.\n')
      sleep(2)
      continue

def pedir_endereco():
  while True:
    limpar_tela()
    print('-'*15, 'Digite o endereço', '-'*15)
    print('\nExemplo: Rua dos Bobos, 0 - São Paulo')
    endereco = input("\nDigite o endereço: ")

    limpar_tela()
    print(f'Você digitou o endereço {endereco}\n')
    confirma = input('Digite S para confirmar ou N para cancelar: ').lower()
    if confirma == 's':
      print(f'\nVocê confirmou o endereço {endereco}\n')
      print('Carregando...')
      geocode = gmaps.geocode(endereco)
      if len(geocode) == 0:
        print('\nEndereço não encontrado, tente novamente.\n')
        sleep(2)
        continue
      else:
        limpar_tela()
        print('-'*15, 'Endereço encontrado','-'*15,)
        print(geocode[0]['formatted_address'])
        print('-'*51)
        
        print('\nEsta é a localização correta?')
        confirma = input('\nDigite S para confirmar ou N para cancelar: ').lower()
        if confirma == 's':
          print('\nEndereço confirmado.\n')
          sleep(2)
          return [geocode[0]['geometry']['location']['lat'], geocode[0]['geometry']['location']['lng']]
        else:
          print('\nVoltando para o menu...\n')
          sleep(2)
          continue
    else:
      print('\nVoltando para o menu...\n')
      sleep(2)
      continue
      

def iniciar_passeio(usuario):
    while True:
      modo_locomocao_escolhido = modo_locomocao()
      if modo_locomocao_escolhido == False:
        return
      tipo_rota_escolhido = escolher_tipo_rota()
      if tipo_rota_escolhido == False:
        return
      if tipo_rota_escolhido == 1:
        rota_escolhida = selecionar_rota()
        if rota_escolhida == False:
          return
        rota = rotas[rota_escolhida]
        limpar_tela()
        print(f'\nVocê escolheu a rota {rota_escolhida} - Rota {rota["nome"]} ({rota["quilometragem"]}km)\n')

        input('\nPressione ENTER para iniciar o passeio...')
        limpar_tela()

        coordenadas_saida = pedir_endereco()
        break

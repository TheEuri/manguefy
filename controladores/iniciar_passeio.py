from time import sleep
import os
from controladores import geolocalizacao

pontos = {
    '1': {
        'nome': 'Monumento ao Manguebeat (Caranguejo da Aurora)',
        'coordenadas': [-8.060745434332873, -34.88080592604645]
    },
    '2': {
        'nome': 'Monumento Caranguejo MangueBeat 2',
        'coordenadas': [-8.064887271787423, -34.874233713306865]
    },
    '3': {
        'nome': 'Memorial Chico Science',
        'coordenadas': [-8.067088267676366, -34.87885749553351]
    },
    '4': {
        'nome': 'Rua da moeda',
        'coordenadas': [-8.064373114500473, -34.872768902089234]
    },
    '5': {
        'nome': 'Memorial arcoverde',
        'coordenadas': [-8.030247061150101, -34.86586451743399]
    },

}

rotas = {
    '1': {
      'nome': 'Manguebeat',
      'pontos': [pontos['1'], pontos['2'], pontos['3'], pontos['4'], pontos['5']],
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
        print('\nVocê escolheu a opção 1 - A pé')
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

def finalizar_passeio(quilometragem, tempo, usuario, nome_rota):
    limpar_tela()
    print(f'Quilometragem: {quilometragem}')
    print(f'Tempo estimado: {tempo}')

    input('\nPressione ENTER para finalizar o seu passeio.')
    limpar_tela()

    with open('./misc/parabens-final-rota.txt', 'r') as parabenizacao:
      print(parabenizacao.read())
    print(f'\n{usuario}, você finalizou com sucesso a rota {nome_rota} (com {quilometragem}).\n')

    input('\nPressione ENTER para voltar ao menu principal.')
    limpar_tela()

def rota_personalizada(pontos):
  pontos_nao_selecionados = []
  pontos_selecionados = []

  for index, ponto in enumerate(pontos):
    pontos_nao_selecionados.append([pontos[ponto]['nome'], pontos[ponto]['coordenadas']])
  
  while True:
    limpar_tela()

    print('-'*15, 'Ponto(s) selecionado(s)', '-'*15)
    if len(pontos_selecionados) == 0:
      print('Nenhum ponto selecionado')
    else:
      for index, ponto in enumerate(pontos_selecionados):
        print(f'{index+1} - {ponto[0]}')
    print('-'*60)
    print('-'*15, 'Opções', '-'*15)
    print('\n1 - Adicionar ponto')
    print('\n2 - Remover ponto')
    print('\n3 - Finalizar rota')
    print('\n4 - Voltar\n')
    print('-'*60)
    opcao = input("\nEscolha uma opção: ")

    limpar_tela()
    if opcao == '1':
      print('-'*15, 'Pontos disponíveis', '-'*15)
      for index, ponto in enumerate(pontos_nao_selecionados):
        print(f'{index+1} - {ponto[0]}')
      print('-'*60)
      ponto_escolhido = input("\nEscolha um ponto: ")

      limpar_tela()
      ponto_valido = False
      for index, ponto in enumerate(pontos_nao_selecionados):
        if ponto_escolhido == str(index+1):
          ponto_valido = True
          pontos_selecionados.append(ponto)
          pontos_nao_selecionados.pop(index)
          print(f'\nVocê adicionou o ponto {ponto[0]}.\n')
          sleep(2)
          break
      if ponto_valido == False:
        print('\nOpção inválida, tente novamente.\n')
        sleep(2)
        continue
    elif opcao == '2':
      if len(pontos_selecionados) == 0:
        print('\nNenhum ponto selecionado\n')
        sleep(2)
        continue
      else: 
        print('-'*15, 'Pontos selecionados', '-'*15)
        for index, ponto in enumerate(pontos_selecionados):
          print(f'{index+1} - {ponto[0]}')
        print('-'*60)
        ponto_escolhido = input("\nEscolha um ponto: ")

        limpar_tela()
        ponto_valido = False
        for index, ponto in enumerate(pontos_selecionados):
          if ponto_escolhido == str(index+1):
            ponto_valido = True
            pontos_nao_selecionados.append(ponto)
            pontos_selecionados.pop(index)
            print(f'\nVocê removeu o ponto {ponto[0]}.\n')
            sleep(2)
            break
        if ponto_valido == False:
            print("Opção invalida, tente novamente.")
            sleep(2)
    elif opcao == '3':
      if len(pontos_selecionados) < 1:
        print('\nVocê precisa selecionar pelo menos 1 ponto para criar uma rota personalizada.\n')
        sleep(2)
        continue
      else:
        pontos_selecionados_para_retornar = []
        for index, ponto in enumerate(pontos_selecionados):
          pontos_selecionados_para_retornar.append({'nome': ponto[0], 'coordenadas': ponto[1]})
        return pontos_selecionados_para_retornar
    elif opcao == '4':
      return False


def iniciar_passeio(usuario):
    try:
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

          coordenadas_saida = geolocalizacao.pedir_endereco()

          sleep(2)
          rota_criada = geolocalizacao.criar_rota(coordenadas_saida, modo_locomocao_escolhido, rota['pontos'])
          mapa = geolocalizacao.criar_mapa(rota_criada, coordenadas_saida, rota['pontos'])

          if mapa == False:
            return
          
          quilometragem = rota_criada[0]['legs'][0]['distance']['text']
          tempo = rota_criada[0]['legs'][0]['duration']['text']

          finalizar_passeio(quilometragem, tempo, usuario, rota['nome'])
          break

        elif tipo_rota_escolhido == 2:
          rota_escolhida = rota_personalizada(pontos)
          if rota_escolhida == False:
            return
          
          limpar_tela()
          coordenadas_saida = geolocalizacao.pedir_endereco()
          sleep(2)

          rota_criada = geolocalizacao.criar_rota(coordenadas_saida, modo_locomocao_escolhido, rota_escolhida)
          mapa = geolocalizacao.criar_mapa(rota_criada, coordenadas_saida, rota_escolhida)

          if (mapa == False):
            return

          quilometragem = rota_criada[0]['legs'][0]['distance']['text']
          tempo = rota_criada[0]['legs'][0]['duration']['text']

          finalizar_passeio(quilometragem, tempo, usuario, 'personalizada')
          break
    except NameError:
      print("Os serviços de localização estão indisponiveis no momento\n Tente novamente abrir o app mais tarde")
      exit()

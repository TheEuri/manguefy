from dotenv import load_dotenv
import googlemaps
import folium
import polyline
import os
from time import sleep

load_dotenv()
gmaps = googlemaps.Client(key=os.environ.get('GOOGLE_API_KEY'))

def limpar_tela():
    # Se for em um dispositivo linux, usa o clear, caso não, usa cls.
    os.system('cls' if os.name == 'nt' else 'clear')

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
      # faz a busca do endereço no google maps
      geocode = gmaps.geocode(endereco)
      if len(geocode) == 0:
        print('\nEndereço não encontrado, tente novamente.\n')
        sleep(2)
        continue
      else:
        limpar_tela()
        print('-'*15, 'Endereço encontrado','-'*15,)
        # retorna o endereço formatado
        print(geocode[0]['formatted_address'])
        print('-'*51)
        
        print('\nEsta é a localização correta?')
        confirma = input('\nDigite S para confirmar ou N para cancelar: ').lower()
        if confirma == 's':
          print('\nEndereço confirmado.\n')
          sleep(2)
          # retorna a latitude e longitude do endereço
          return [geocode[0]['geometry']['location']['lat'], geocode[0]['geometry']['location']['lng']]
        else:
          print('\nVoltando para o menu...\n')
          sleep(2)
          continue
    else:
      print('\nVoltando para o menu...\n')
      sleep(2)
      continue

def criar_rota(saida, modo_locomocao, pontos):
  vetor_pontos = []

  for ponto in pontos:
    vetor_pontos.append(ponto['coordenadas'])

  ponto_final = vetor_pontos.pop()

  modo_locomocao_maps = ''

  if modo_locomocao == '1':
    modo_locomocao_maps = 'walking'
  elif modo_locomocao_maps == '2':
    modo_locomocao_maps = 'transit'
  elif modo_locomocao == '3':
    modo_locomocao_maps = 'bicycling'

  print(modo_locomocao_maps)

  rota = gmaps.directions(saida, ponto_final, mode=modo_locomocao_maps, waypoints=vetor_pontos)

  return rota

def criar_mapa(rota, saida, pontos):

  polyline_decodificado = polyline.decode(rota[0]['overview_polyline']['points'])
  mapa = folium.Map(location=saida,  zoom_start=13)
  folium.Marker((saida[0], saida[1]), popup='Ponto de partida').add_to(mapa)
  for index, ponto in enumerate(pontos):
    folium.Marker((ponto['coordenadas'][0], ponto['coordenadas'][1]), popup=f"{index+1}. {ponto['nome']}", icon=folium.Icon(color='red', icon='asterisk')).add_to(mapa)
  folium.PolyLine(polyline_decodificado, weight=5, opacity=1).add_to(mapa)
  mapa.save('mapa.html')
  print('Mapa criado com sucesso!')

  return

  
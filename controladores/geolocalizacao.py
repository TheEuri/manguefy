from dotenv import load_dotenv
import googlemaps
import folium
import polyline
import os
from time import sleep
import webbrowser

load_dotenv()
try: 
  gmaps = googlemaps.Client(key=os.environ.get('GOOGLE_API_KEY'))
except:
  print('Não foi possível conectar ao Google Maps, verifique sua conexão com a internet ou se sua chave de API é válida.')
    
def limpar_tela():
    # Se for em um dispositivo linux, usa o clear, caso não, usa cls.
    os.system('cls' if os.name == 'nt' else 'clear')

def pedir_endereco():
  try:
    while True:
      limpar_tela()
      print('-'*15, 'Digite o seu endereço', '-'*15)
      print('\nExemplo: Rua dos Bobos, 0 - São Paulo')
      endereco = input("\nDigite o endereço: ")
      if endereco.strip() =="":
        print("O endereco não pode ser vazio.")
        sleep(2)
        continue

      limpar_tela()
      print(f'Você digitou o endereço {endereco}\n')
      confirma = input('Digite S para confirmar ou N para cancelar: ').lower()
      if confirma == 's':
        print(f'\nVocê confirmou o endereço {endereco}\n')
        print('Carregando...')
        # faz a busca do endereço no google maps
        try:
          geocode = gmaps.geocode(endereco)
        except:
          print('Não foi possível conectar ao Google Maps, verifique sua conexão com a internet ou se sua chave de API é válida.')
          exit()
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
        print('\nNessa etapa é necessário digitar um endereço.\n')
        sleep(5)
        continue
  except NameError:
      print("Os serviços de localização estão indisponiveis no momento\n Tente novamente abrir o app mais tarde")
      exit()
            
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

  try:
    rota = gmaps.directions(saida, ponto_final, mode=modo_locomocao_maps, waypoints=vetor_pontos)
  except:
    print('Não foi possível criar uma rota, tente novamente mais tarde.')
    exit()
  return rota

def criar_mapa(rota, saida, pontos):
  try:
    polyline_decodificado = polyline.decode(rota[0]['overview_polyline']['points'])
    mapa = folium.Map(location=saida,  zoom_start=13)
    folium.Marker((saida[0], saida[1]), popup='Ponto de partida').add_to(mapa)
    for index, ponto in enumerate(pontos):
      folium.Marker((ponto['coordenadas'][0], ponto['coordenadas'][1]), popup=f"{index+1}. {ponto['nome']}", icon=folium.Icon(color='red', icon='asterisk')).add_to(mapa)
    folium.PolyLine(polyline_decodificado, weight=5, opacity=1).add_to(mapa)
    mapa.save('mapa.html')
  except:
    print('Não foi possível criar o mapa, tente novamente mais tarde.')
    exit()

  while True:
    limpar_tela()
    print('-'*15, 'Iniciar passeio', '-'*15)
    print('Deseja iniciar o passeio?')
    confirma = input('\nDigite S para confirmar ou N para cancelar: ').lower()
    if confirma == 's':
      print('\nIniciando passeio...\n')
      sleep(2)
      webbrowser.open('mapa.html')
      return True
    if confirma == 'n':
      print('\nVoltando para o menu...\n')
      sleep(2)
      return False
    else:
      continue


  
  

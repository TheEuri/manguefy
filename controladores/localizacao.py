import os
import time

def limpar_tela():
    # Se for em um dispositivo linux, usa o clear, caso não, usa cls.
    os.system('cls' if os.name == 'nt' else 'clear')

def verificar_permissao_localizacao(usuario):
    # Tenta abrir o arquivo, se não existir, cria um novo.
    open('./dados/localizacao.txt', 'a').close()
    if usuario == 'VISTANTE':
        return
    arquivo = open('./dados/localizacao.txt', 'r')
    localizacao = arquivo.readlines()
    arquivo.close()
    for aceites in localizacao:
        escolhaUsuario = aceites.strip().split('|')
        if escolhaUsuario[0] == usuario:
            if escolhaUsuario[1] == '1':
                return True


def pedir_permissao_localizacao(usuario):
    arquivo = open('./dados/localizacao.txt', 'a')

    print('-' * 35, 'Entenda melhor a nossa proposta', '-' * 35)
    print('O aplicativo funciona através de geolocalização, ativando sons específicos ao passar por pontos \nturísticos da cidade de Recife. Por isso, para o funcionamento do Manguefy, é necessário a permissão \ndo acesso a sua localização.')
    print('-' * 103)

    escolha = input('\nDeseja permitir o acesso a sua localização? (S/N): ')
    aceito = False
    if escolha.lower() == 's':
        print('Permissão concedida.')
        time.sleep(2)
        limpar_tela()
        if not usuario == 'VISITANTE':
            arquivo.write(usuario + '|' + '1' + '\n')
        aceito = True
    else:
        print('O aplicativo precisa utilizar a sua localização para funcionar adequadamente.')
        time.sleep(2)
    arquivo.close()

    return aceito
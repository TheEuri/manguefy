import os
import time

def limpar_tela():
    # Se for em um dispositivo Ios, usa o clear, caso não, usa cls.
    os.system('cls' if os.name == 'nt' else 'clear')

def verificar_permissao_localizacao(usuario):
    # Tenta abrir o arquivo, se não existir, cria um novo.
    open('localizacao.txt', 'a').close()
    if usuario == 'VISTANTE':
        return
    arquivo = open('localizacao.txt', 'r')
    localizacao = arquivo.readlines()
    arquivo.close()
    for aceites in localizacao:
        escolhaUsuario = aceites.strip().split('|')
        if escolhaUsuario[0] == usuario:
            if escolhaUsuario[1] == '1':
                return True


def pedir_permissao_localizacao(usuario):
    arquivo = open('localizacao.txt', 'a')
    escolha = input('Deseja permitir o acesso a sua localização? (S/N): ')
    aceito = False
    if escolha.lower() == 's':
        print('Permissão concedida.')
        time.sleep(2)
        limpar_tela()
        if not usuario == 'VISITANTE':
            arquivo.write(usuario + '|' + '1' + '\n')
        aceito = True
    else:
        print('Texto explicando que o acesso a localização é necessário para o funcionamento do programa.')
    arquivo.close()

    return aceito
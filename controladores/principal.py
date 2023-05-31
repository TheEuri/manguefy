def verificarPermisaoLocalizacao():
    arquivo = open('localizacao.txt', 'r')
    localizacao = arquivo.read()
    arquivo.close()
    if localizacao == '1':
        return True
    else:
        return False
  
def pedirPermissaoLocalizacao():
    arquivo = open('localizacao.txt', 'w')
    escolha = input('Deseja permitir o acesso a sua localização? (S/N): ')
    if escolha.lower() == 's':
        arquivo.write('1')
    else:
        print('Texto explicando que o acesso a localização é necessário para o funcionamento do programa.')
        arquivo.write('0')
    arquivo.close()
  

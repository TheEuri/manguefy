from controladores import autenticacao
from controladores import localizacao
from controladores import informacoes
from time import sleep

while True:
    with open('./misc/manguefy-logo.txt', 'r') as logo:
        print(logo.read())
        print("Iniciando...")
        sleep(2)
        localizacao.limpar_tela()
    informacoes.informacoes()
    usuario_atual = autenticacao.menu_cadastro_login()

    if usuario_atual == '\sair_programa':
        break
    else:
        loop_localizacao = True
        while loop_localizacao:
            localizacao.limpar_tela()
            permissao = localizacao.verificar_permissao_localizacao(usuario_atual)
            if permissao:
                loop_localizacao = False
            else:
                loop_localizacao = not localizacao.pedir_permissao_localizacao(usuario_atual)
        break
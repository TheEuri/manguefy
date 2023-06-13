try:
    import os
    os.system("cls")
    from controladores import autenticacao
    from controladores import localizacao
    from controladores import sobre
    from controladores.menu_principal import menu_principal

    while True:
        sobre.boasvindas()

        # Mostra o menu de cadastro e login
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

            menu_principal(usuario_atual)
            break
except:
    print("A instalação não foi concluida corretamente.")

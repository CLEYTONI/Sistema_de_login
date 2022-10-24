def newcadastro():
    from time import sleep
    import PySimpleGUI as sg
    conta = {'Login': '', 'Senha': ''}  # Criando dicionario para que a estrutura de repetição fucione.
    while not conta['Login'][-1:-11:-1][::-1] == '@gmail.com':
        error = False
        # DEFININDO LAYOUT DO CADASTRO
        sg.theme('DarkAmber')
        layout = [[sg.Text(f'{"NOVO CADASTRO":^90}', text_color='black')],
        [sg.Text('E-mail:', text_color='black'), sg.InputText()],
        [sg.Text('Senha:', text_color='black'), sg.InputText()],
        [sg.Button('PROSSEGUIR'), sg.Text(' ' * 60), sg.Button('CANCELAR')]]
        cadastro = sg.Window('BASKARA', layout)

        # SALAVANDO OS DADOS DO USUARIO TEMPORARIAMENTE
        dados_usuario = cadastro.Read()
        cadastro.close()

        # VERIFICANDO SE O USUARIO CANCELOU O PROCESSO
        if dados_usuario[0] == None or dados_usuario[0] == 'CANCELAR':
            cacelar = [[sg.Text('  OPERAÇÃO CANCELADA!', text_color='red')],
                       [sg.Text('DADOS NÃO CASDASTRADOS!', text_color='red')],
                       [sg.Text(' ' * 16), sg.Button('OK', button_color='white')]]
            cacelar = sg.Window('BASKARA', cacelar)
            print(cacelar.read())
            cacelar.close()
            return False

        # VERIFICANDO SE O LOGIN TEM FORMATO GMAIL VÁLIDO
        if not dados_usuario[1][0][-1:-11:-1][::-1] == '@gmail.com':
            print('\033[31mE-mail inválido!\033[m')
            error = True
            # continue

        # VERIFICANDO SE A SENHA TEM NO MINIMO 8 CARACTERES
        if len(dados_usuario[1][1]) < 8:
            conta = {'Login': '', 'Senha': ''}
            print('\033[31mSenha deve ter no minímo 8 caracteres!\033[m')
            error = True
            # continue

        # VARIAVEL ERROR RECEBERA TRUE CASO A CONDIÇÃO GMAIL OU A CONDIÇÃO SENHA NÃO SEJA ATENDIDA
        if error:
             continue

        # PREPARANDO OS DADOS PARA JOGAR PARA O "BANCO DE DADOS"
        conta = {'Login': dados_usuario[1][0], 'Senha': dados_usuario[1][1]}

        # ANUNCIANDO ENCERRAMENTO
        print('Finalizando cadastro aguarde...')
        sleep(3)  # atraso proposital pra dá o tcham kkk

        # JOGANDO OS DADO PARA O "BANCO DE DADOS"
        bd = 'bd.txt'
        bd = open(bd, 'at')
        bd.write(f"{conta['Login']}\n{conta['Senha']}")
        bd.close()

        # MENSAGEM FINAL DE CONCLUSÃO APÓS VERIFICAR POSSIVEIS ERROS
        concluido = [[sg.Text('CADASTRO FINALIZADO COM SUCESSO ✅', text_color='green')],
                     [sg.Text(' ' * 25), sg.Button('OK', button_color='white')]]
        concluido = sg.Window('BASKARA', concluido)
        concluido.read()
        concluido.close()
        print('\033[32mConcluído\033[m')
        # FIM DO PROGRAMA NOVO CADASTRO EFETUADO COM SUCESSO!!


def login():
    import PySimpleGUI as sg
    from time import sleep
    c = 0

    while True:
        error = False

        # DEFINDO O LAYOUT DE LOGIN
        layout = [[sg.Text(f'{"ENTRAR":^90}', text_color='black')],
                  [sg.Text('Login:', text_color='black'), sg.InputText()],
                  [sg.Text('Senha', text_color='black'), sg.InputText()],
                  [sg.Button('PROSSEGUIR'), sg.Text(' ' * 60), sg.Button('CANCELAR')]]
        dados_usuario = sg.Window('BASKARA', layout)
        login = dados_usuario.Read()
        dados_usuario.close()

        # VERIFICANDO SE O USUARIO CANCELOU A OPERAÇÃO
        if login[0] == sg.WIN_CLOSED or login[0] == 'CANCELAR':
            cancelar = [[sg.Text('OPERAÇÃO CANCELADA!', text_color='red')],
                        [sg.Text(' ' * 14), sg.Button('OK')]]
            cacelado = sg.Window('BASKARA', cancelar)
            cacelado.Read()
            cacelado.close()
            return False

        # PEGANDO NO "BANCO DE DADOS" A SENHA E O LOGIN
        conta = {'Login': '', 'Senha': ''}
        conta['Login'], conta['Senha'] = open('bd.txt', 'rt'), open('bd.txt', 'rt')
        conta['Login'], conta['Senha'] = conta['Login'].readlines()[0][-2::-1][::-1], conta['Senha'].readlines()[1]

        # VERIFICANDO SE O GMAIL CORRESPONDE AO DO "BANCO DE DADOS"
        print('Verificando E-mail...')
        sleep(1.5)
        if not login[1][0] == conta['Login']:
            error = True
            print('\033[31mLogin invalido\033[m')
            continue
        else:
            c += 1
            print('\033[32mLogin está correto\033[m')

        sleep(1.5)

         # VERIFINCANDO A SE A SENHA CORRESPONDE AO DO "BANCO DE DADOS"
        print('Confirmando Senha...')
        sleep(1.5)
        if not login[1][1] == conta['Senha']:
            error = True
            print('\033[31mSenha Invalida\033[m')
        else:
            print('\033[32mSenha está correta\033[m')

        # VERIFICANDO SE ELE FEZ 3 TENTATIVAS COM O MESMO LOGIN
        if c == 3:
            print('\033[31mNúmero de tentativas excedido.\033[m')
            print('Essa conta será bloqueada por 1h até as proxímas tentativas')
            return False

        if error:
            continue
        sleep(1.5)
        print('Conectando ao servidor...')
        sleep(3)
        # MENSAGEM FINAL DE CONCLUSÃO
        sg.theme('DarkAmber')
        concluir = [[sg.Text('CONEXÃO REALIZADA COM SUCESSO', text_color='green')],
                    [sg.Text('        BEM VINDO AO BASKARA', text_color='green')],
                    [sg.Text(' ' * 23), sg.Button('OK')]]
        concluir = sg.Window('BASKARA', concluir)
        concluir.Read()
        concluir.close()
        return True


def limpa_cadastro():
    open('bd.txt', 'w').close()
    print('\033[32mCadastro Excluido Com Sucesso!\033[m')

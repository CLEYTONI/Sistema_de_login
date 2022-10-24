import Cadastro
from time import sleep
Logado = None
print('''BEM VINDO AO BASKARA SYSTEM''')


while True:
    print('''
[1] NOVO CADASTRO
[2] LOGAR
[3] EXCLUIR LOGIN
[4] SAIR
    ''')

    usuario = input('ESCOLHA:')
    # OPÇÃO 1 DO USUARIO
    if usuario == '1':
        # verificando se ja não existe uma conta no "banco de dados"
        conta = open('bd.txt', 'rt')
        conta = conta.readlines()
        if conta != []:
            print('\033[31mConta existente!Não é possivél cadastra uma nova.\033[m')
            continue
        # caso não haja nada segue para o comando de cadastro
        Cadastro.newcadastro()

    # OPÇÃO 2 DO USUARIO
    elif usuario == '2':
        # verificando se ele não logou ainda
        if Logado:
            print('\033[33mVocê já está logado!!\033[m')
            continue
        # verificando se tem alguma conta cadastrada para não da error
        situacao_arquivo = open('bd.txt', 'rt')
        if situacao_arquivo.read() == '':
            print('\033[31mO Cadastro ainda não foi efetuado!!\033[m')
            continue
        # caso as condições acima seja atendidas seguirá para o comando de login
        Logado = Cadastro.login()
        if Logado:
            print('\033[32mVocê está logado!!\033[m')
        else:
            print('\033[31mVocê não está logado!!\033[m')

    # OPÇÃO 3 DO USUSARIO
    elif usuario == '3':
        # verificando se tem alguma conta cadastrada para não da error
        situacao_arquivo = open('bd.txt', 'rt')
        if situacao_arquivo.read() == '':
            print('\033[31mNenhuma conta exitente!!\033[m')
            continue
        # caso exista uma conta segue para o comando de exclusão
        print('Desconectando...')
        Logado = False
        sleep(1)
        Cadastro.limpa_cadastro()

    # OPÇÃO 4 O USUARIO
    elif usuario == '4':
        if Logado:
            print('Desconectando...')
            Logado = False
            sleep(1)
        print('Finalizado! Obrigado por vim.')
        break


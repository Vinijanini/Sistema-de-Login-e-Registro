import sqlite3
import time
import pyautogui as py
from selenium import webdriver
from selenium.webdriver.common.by import By

banco = sqlite3.connect('banco_de_dados.db')
cursor = banco.cursor()

##Verifica se existe uma tabela, se não, crie uma##
ver = cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='infos';").fetchone()
if ver[0] == 0:
    cursor.execute("CREATE TABLE infos (nome text, email text, idade int, sexo text, login text, senha text)")

##Váriáveis globais##
usuarios = []
usuario = {}
acess= None

##Funções##
def lin2():
    print('-' * 20)


def lin():
    print('-=' * 10)


def menu():
    lin()
    print('[1] Logar')
    print('[2] Registrar')
    print('[3] Ver Cadastrados')
    print('[4] Entrar de ADM')
    print('[5] Sair')
    lin()


def menulogado():
    lin()
    print('[1] Apagar conta')
    print('[2] Sair')
    lin()


def adm():
    lin()
    print('[1] Banir conta')
    print('[2] Cadastrados')
    print('[3] Enviar email')
    print('[4] Sair')
    lin()


while True:
    menu()
    esc = str(input('>>>>>>>>>>>>>>'))

    ##Tratamento de erro##
    while esc not in ('1','2','3','4','5'):
        print('Erro, Opção inválida')
        esc = str(input('>>>>>>>>>>>>>>'))

    cursor.execute("SELECT * FROM infos")
    cli = cursor.fetchall()

    ##tratamento de erro##
    while esc in ('1','3') and len(cli) == 0:
        print('Erro! Ainda nao há conta cadastrada')
        menu()
        esc = str(input('>>>>>>>>>>>>>>'))

    ##registro##
    if esc == '2':
        lin()
        print('Registro')
        usuario['Nome'] = str(input('Nome:')).title()
        usuario['Email'] = str(input('Email:'))
        usuario['Idade'] = int(input('Idade:'))

        ##Tratamento de erro##
        while usuario['Idade'] not in range(10, 80):
            print('Erro! Digite uma idade real')
            usuario['Idade'] = int(input('Idade:'))
        usuario['Sexo'] = str(input('Sexo[m/f]:')).lower()

        ##Tratamento de erro##
        while usuario['Sexo'] not in ('m','f'):
            print('Erro!')
            usuario['Sexo'] = str(input('Sexo[m/f]:')).lower()
        usuario['Login'] = str(input('Login:'))

        #Se o login já existir, da erro##
        for conta in usuarios:
            while conta['Login'] == usuario['Login']:
                print('Erro, Usuário existente.')
                usuario['Login'] = str(input('Login:'))
        cursor.execute("SELECT * FROM infos")
        clientes = cursor.fetchall()
        for c in clientes:
            if usuario['Login'] == c[4]:
                print('Erro, Usuário existente.')
                usuario['Login'] = str(input('Login:'))

        ##Cadastra senha da conta##
        usuario['Senha'] = str(input('Senha:'))
        confirm_senha = str(input('Confirmar senha:'))

        ##Confirmação se senhas iguais##
        while usuario['Senha'] != confirm_senha:
            lin2()
            print('Erro, senhas diferentes.')
            usuario['Senha'] = str(input('Senha:'))
            confirm_senha = str(input('Confirmar senha:'))
        lin()

        ##Insere os dados no SQLite##
        cursor.execute("SELECT * FROM infos")
        cursor.execute("INSERT INTO infos VALUES('"+usuario['Nome']+"','"+usuario['Email']+"',"+str(usuario['Idade'])+",'"+usuario[
            'Sexo']+"','"+usuario['Login']+"','"+usuario['Senha']+"')")
        banco.commit()
        usuarios.append(usuario.copy())
        print('Perfil Cadastrado com sucesso!')

    ##Login##
    elif esc == '1':
        loginlog = str(input('Login:'))
        senhalog = str(input('Senha:'))
        cursor.execute("SELECT * FROM infos")
        clientes = cursor.fetchall()

        ##Verifica se Login e senha existem no banco de dados, se sim, o acesso é aceito##
        for c in clientes:
            if loginlog == c[4] and senhalog == c[5]:
                acess = True
                lin2()
                print(f'Bem-Vindo(a) - {c[0]}')
                nome_logado = c[0]
                lin2()
                print(f'Sua idade - {c[1]}')
                lin2()
                if c[2] == 'm':
                    print(f'Seu sexo é Masculino')
                else:
                    print(f'Seu sexo é Feminino')
                lin2()
                print(f'Seu id é "{clientes.index(c)+1}"')
                lin2()
        for cliente in usuarios:
            if cliente['Login'] == loginlog and cliente['Senha'] == senhalog:
                logado = cliente
                break

        ##Se acesso negar, mensagem de erro##
        if acess != True:
            print('Usuário ou senha inválidos')

        ##logou na conta##
        while acess == True:
            while True:
                menulogado()
                esc2 = str(input('>>>>>>>>>'))
                lin2()

                ##Deslogar##
                if esc2 == "2":
                    acess = False
                    break

                ##Tratamento de erro##
                while esc2 not in ('1','2'):
                    print("opção inválida!")

                ##Apagar conta##
                while esc2 == "1":
                        print('Apagar conta!!')
                        print('Digite "2" para voltar')
                        senha_apagar = str(input('Digite sua senha para excluir sua conta:'))

                        ##Digite 2, para cancelar o apagamento da conta##
                        if senha_apagar == "2":
                            break
                        while senha_apagar != senhalog:
                            print('Senha inválida!')
                            print('Digite "2" para voltar')
                            senha_apagar = str(input('Digite sua senha para excluir sua conta:'))
                            if senha_apagar == "2":
                                break
                        if senha_apagar == "2":
                            break

                        ##Apaga conta##
                        else:
                            if senha_apagar == senhalog:
                                cursor.execute("DELETE from infos WHERE nome = '"+nome_logado+"'")
                                banco.commit()
                                lin()
                                print('Conta deletada com sucesso')
                                lin()
                                acess = False
                                logado = False
                                break

                ##Desloga##
                if acess == False:
                    break

    ##Exibe os usuários cadastrados
    elif esc == '3':
        cursor.execute("SELECT * FROM infos")
        for cont,c2 in enumerate(cursor.fetchall()):
            time.sleep(0.7)
            print(f'{cont+1}º Perfil cadastrado')
            lin2()
            for cont, c3 in enumerate(c2):
                if cont == 0:
                    print(f'Nome:{c3}')
                elif cont == 2:
                    print(f'Idade:{c3}')
            lin()
    ##Logar de ADM##
    elif esc == '4':
        while True:
            login = 'adm102030'
            senha = '@Az1310750412'
            log_adm = str(input('Login ADM:'))
            sen_adm = str(input('Senha ADM:'))
            lin()
            if login == log_adm and senha == sen_adm:
                ##Entrou de ADM##
                while True:
                    print('Sistema de Administração')
                    adm()
                    esc_adm = str(input('>>>>>>>>>>>>>'))
                    while esc_adm not in ('1','2','3','4'):
                        print('Opção inválida!')
                        esc_adm = str(input('>>>>>>>>>>>>>'))
                    ##Banir conta##
                    if esc_adm == '1':
                        log_ban = str(input('Login da conta que irá apagar:'))
                        cursor.execute("SELECT * FROM infos")
                        conf = None
                        for c2 in cursor.fetchall():
                            if c2[4] == log_ban:
                                conf = True
                                cursor.execute("DELETE from infos WHERE login = '" + log_ban + "'")
                                banco.commit()
                                print('Conta apagada com sucesso')
                                lin()
                        if conf != True:
                            print('Login inválido!')
                            lin()
                    ##Exibir informações dos cadastrados##
                    if esc_adm == '2':
                        cursor.execute("SELECT * FROM infos")
                        for cont, c2 in enumerate(cursor.fetchall()):
                            time.sleep(0.7)
                            print(f'{cont + 1}º Perfil cadastrado')
                            lin2()
                            for cont, c3 in enumerate(c2):
                                if cont == 0:
                                    print(f'Nome:{c3}')
                                elif cont == 1:
                                    print(f'Email:{c3}')
                                elif cont == 2:
                                    print(f'Idade:{c3}')
                                elif cont == 3:
                                    if c3 == 'm':
                                        print('Sexo:Masculino')
                                    else:
                                        print('Sexo:Feminino')
                                elif cont == 4:
                                    print(f'Login:{c3}')
                                elif cont == 5:
                                    print(f'Senha:{c3}')
                            lin()

                    ##Enviar email##
                    if esc_adm == '3':
                        email_log = str(input('Login do usuário que irá receber o email:'))
                        cursor.execute("SELECT * FROM infos")
                        conf = None
                        for c in cursor.fetchall():
                            if email_log == c[4]:
                                conf = True
                                print('O programa irá rodar seu navegador automaticamente!!!')
                                print('Não interrompa até a mensagem de liberação!!!')
                                print('Iniciando em 7 segundos...')
                                time.sleep(7)
                                navegador = webdriver.Chrome()
                                navegador.get('https://login.live.com/')
                                navegador.find_element(By.XPATH, '//*[@id="i0116"]').send_keys('AdmViniPy@hotmail.com')
                                navegador.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
                                navegador.find_element(By.XPATH, '//*[@id="i0118"]').send_keys('@Az1310750412')
                                time.sleep(3)
                                navegador.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
                                navegador.find_element(By.XPATH, '//*[@id="idBtn_Back"]').click()
                                time.sleep(10)
                                navegador.find_element(By.XPATH,'//*[@id="home.cards.card.outlook.cold"]/div[4]/a/span').click()
                                time.sleep(6)
                                py.press('n')
                                time.sleep(3)
                                py.write(c[1])
                                print('Você está liberado para mexer novamente!')
                                lin()
                        if conf != True:
                            print('Login inválido!!')
                            lin()

                    ##Sair do programa##
                    if esc_adm == '4':
                        print('Deslogando...')
                        time.sleep(1)
                        break
                break
            else:
                print('Login ou senha inválidos')
                break

    ##programa finaliza##
    elif esc == '5':
        input('Programa finalizado')
        quit()
import sqlite3
import time
cont2 = 0
banco = sqlite3.connect('banco_de_dados.db')
cursor = banco.cursor()

ver = cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='infos';").fetchone()
if ver[0] == 0:
    cursor.execute("CREATE TABLE infos (nome text, idade int, sexo text, login text, senha text)")

usuarios = []
usuario = {}
acess= None
def lin2():
    print('-' * 20)
def lin():
    print('-=' * 10)
def menu():
    lin()
    print('[1] Logar')
    print('[2] Registrar')
    print('[3] Ver Cadastrados')
    print('[4] Sair')
    lin()
def menulogado():
    lin()
    print('[1] Apagar conta')
    print('[2] Sair')
    lin()


while True:
    menu()
    esc = str(input('>>>>>>>>>>>>>>'))
    while esc not in '1234':
        print('Erro, Opção inválida')
        esc = str(input('>>>>>>>>>>>>>>'))
    cursor.execute("SELECT * FROM infos")
    cli = cursor.fetchall()
    while esc in '13' and len(cli) == 0:
        print('Erro! Ainda nao há conta cadastrada')
        menu()
        esc = str(input('>>>>>>>>>>>>>>'))
    if esc == '2':
        lin()
        print('Registro')
        usuario['Nome'] = str(input('Nome:'))
        usuario['Nome']
        usuario['Idade'] = int(input('Idade:'))
        while usuario['Idade'] not in range(10, 80):
            print('Erro! Digite uma idade real')
            usuario['Idade'] = int(input('Idade:'))
        usuario['Sexo'] = str(input('Sexo[m/f]:')).lower()
        while usuario['Sexo'] not in 'mf':
            print('Erro!')
            usuario['Sexo'] = str(input('Sexo[m/f]:')).lower()
        usuario['Login'] = str(input('Login:'))
        for conta in usuarios:
            while conta['Login'] == usuario['Login']:
                print('Erro, Usuário existente.')
                usuario['Login'] = str(input('Login:'))
        cursor.execute("SELECT * FROM infos")
        clientes = cursor.fetchall()
        for c in clientes:
            if usuario['Login'] == c[3]:
                print('Erro, Usuário existente.')
                usuario['Login'] = str(input('Login:'))
        usuario['Senha'] = str(input('Senha:'))
        confirm_senha = str(input('Confirmar senha:'))
        while usuario['Senha'] != confirm_senha:
            lin2()
            print('Erro, senhas diferentes.')
            usuario['Senha'] = str(input('Senha:'))
            confirm_senha = str(input('Confirmar senha:'))
        lin()

        cursor.execute("SELECT * FROM infos")
        cursor.execute("INSERT INTO infos VALUES('"+usuario['Nome']+"',"+str(usuario['Idade'])+",'"+usuario[
            'Sexo']+"','"+usuario['Login']+"','"+usuario['Senha']+"')")
        banco.commit()

        usuarios.append(usuario.copy())
        print('Perfil Cadastrado com sucesso!')
    elif esc == '1':
        loginlog = str(input('Login:'))
        senhalog = str(input('Senha:'))
        cursor.execute("SELECT * FROM infos")
        clientes = cursor.fetchall()

        for c in clientes:
            if loginlog == c[3] and senhalog == c[4]:
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
        if acess != True:
            print('Usuário ou senha inválidos')
        ##logou na conta##
        while acess == True:
            while True:
                menulogado()
                esc2 = str(input('>>>>>>>>>'))
                lin2()
                if esc2 == "2":
                    acess = False
                    break
                while esc2 not in '12':
                    print("opção inválida!")
                while esc2 == "1":
                        print('Apagar conta!!')
                        print('Digite "2" para voltar')
                        senha_apagar = str(input('Digite sua senha para excluir sua conta:'))
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
                if acess == False:
                    acess = False
                    break
    elif esc == '3':
        cursor.execute("SELECT * FROM infos")
        for cont,c2 in enumerate(cursor.fetchall()):
            time.sleep(0.7)
            print(f'{cont+1}º Perfil cadastrado')
            lin2()
            for cont, c3 in enumerate(c2):
                if cont == 0:
                    print(f'Nome:{c3}')
                elif cont == 1:
                    print(f'Idade:{c3}')
            lin()
    elif esc == '4':
        break
input('Programa finalizado')
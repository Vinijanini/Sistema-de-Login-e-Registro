import sqlite3
banco = sqlite3.connect('banco_de_dados.db')
cursor = banco.cursor()

ver = cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='infos';").fetchone()
if ver[0] == 0:
    cursor.execute("CREATE TABLE infos (nome text, idade int, sexo text, login text, senha text)")

usuarios = []
usuario = {}
acess= None
acess2 = None
def lin2():
    print('-' * 20)
def lin():
    print('-=' * 10)
def menu():
    lin()
    print('[1] Logar')
    print('[2] Registrar')
    lin()
while True:
    menu()
    esc = str(input('>>>>>>>>>>>>>>'))
    while esc not in '12':
        print('Erro, Opção inválida')
        esc = str(input('>>>>>>>>>>>>>>'))
    cursor.execute("SELECT * FROM infos")
    cli = cursor.fetchall()
    while esc == '1' and len(cli) == 0:
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
        lin()
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
                lin2()
                print(f'Sua idade - {c[1]}')
                lin2()
                if c[2] == 'm':
                    print(f'Seu sexo é Masculino')
                else:
                    print(f'Seu sexo é Feminino')
                lin2()
                print(f'Seu id é "{clientes.index(c)}"')
                lin2()
        for cliente in usuarios:
            if cliente['Login'] == loginlog and cliente['Senha'] == senhalog:
                logado = cliente
                acess2 = True
                break
            else:
                acess2 = False
        if acess2 == True:
            acess = True
        elif acess2 == False:
            acess = False
        if acess == True:
            break
        elif acess == False:
            lin()
        print('Usuário ou Senha Inválidos!')
input('Programa finalizado')
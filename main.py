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
def log():
    lin2()
    print(f'Bem-Vindo(a) - {logado["Nome"]}')
    lin2()
    print(f'Sua idade - {logado["Idade"]}')
    lin2()
    if logado['Sexo'] == 'm':
        print(f'Seu sexo é Masculino')
    else:
        print(f'Seu sexo é Feminino')
    lin2()
    print(f'Seu id é "{usuarios.index(logado)}"')
    lin2()
while True:
    menu()
    esc = str(input('>>>>>>>>>>>>>>'))
    while esc not in '12':
        print('Erro, Opção inválida')
        esc = str(input('>>>>>>>>>>>>>>'))
    while esc == '1' and len(usuarios) == 0:
        print('Erro! Ainda nao há conta cadastrada')
        menu()
        esc = str(input('>>>>>>>>>>>>>>'))
    if esc == '2':
        lin()
        print('Registro')
        usuario['Nome'] = str(input('Nome:'))
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
        usuario['Senha'] = str(input('Senha:'))
        lin()
        usuarios.append(usuario.copy())
        print('Perfil Cadastrado com sucesso!')
    elif esc == '1':
        loginlog = str(input('Login:'))
        senhalog = str(input('Senha:'))
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
    if acess == False:
        lin()
        print('Usuário ou Senha Inválidos!')
    elif acess == True:
        break
log()
input('Programa finalizado')
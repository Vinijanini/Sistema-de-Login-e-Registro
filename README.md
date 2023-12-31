Este programa em Python implementa um sistema de cadastro e login com armazenamento de informações em um banco de dados SQLite. O objetivo é permitir que usuários criem perfis, acessem suas informações após o login, visualizem perfis cadastrados e, se desejarem, apaguem suas contas.

Funcionalidades Principais:
1. Logar:
Os usuários têm a opção de registrar um perfil fornecendo informações como nome, idade, sexo, login e senha. O programa verifica se o login já existe, se a idade está dentro de um intervalo válido e se a senha foi confirmada corretamente. Os perfis são armazenados na tabela "infos" do banco de dados.

2. Registrar:
Os usuários podem realizar o login fornecendo seu nome de usuário e senha. O programa verifica as credenciais no banco de dados e, se autenticado com sucesso, exibe informações sobre o usuário logado, como nome, idade e sexo.

3. Visualizar Perfis Cadastrados:
Os usuários podem visualizar uma lista de todos os perfis cadastrados, exibindo seus nomes e idades. Essa informação é obtida a partir da consulta ao banco de dados.

4. Entrar como Administrador:
Usuários autenticados têm a opção de apagar suas contas. Eles devem confirmar a exclusão digitando novamente sua senha. O programa remove a conta correspondente do banco de dados.
LOGIN: adm102030
SENHA: @Az1310750412

6. Encerrar o Programa:
Os usuários podem encerrar o programa a qualquer momento selecionando a opção correspondente.

Conclusão:
Este programa fornece uma funcionalidade básica de cadastro e login, utilizando um banco de dados SQLite para armazenar informações dos usuários. Há espaço para aprimoramentos em termos de segurança, usabilidade e estrutura do código.

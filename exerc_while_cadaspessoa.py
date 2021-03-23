'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

print('-=' * 30)
print('\33[0;40;41m CADASTRO DE PESSOAS \33[m')
print('-=' * 30)
tot18 = 0
masc = 0
fem = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M /F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 =+ 1
    if sexo == 'M':
        masc += 1
    if sexo == 'M' and idade < 20:
        fem += 1
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Deseja cadastrar mais usuários [S ou N]? ')).strip().upper()[0]
    if pergunta == 'N':
        break
print(f'O Total de pessoas com mais de 18 anos: {tot18}')
print(f'O Total de Homens cadastrados são: {masc}')
print(f'O Total de Mulhere cadastradas com menos de 20 anos são: {fem}')



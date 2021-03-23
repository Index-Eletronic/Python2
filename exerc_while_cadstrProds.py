'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

totprod = 0
prodcaro = 0
nomebarato = ' '
cont = 0
menor = 0
while True:
    prod = str(input('Digete o nome do produto: ')).strip().upper()
    preco = float(input('Digite o valor do produto R$:'))
    cont += 1
    if preco > 0:
        totprod += preco
    if cont == 1 or preco < menor:
        menor = preco
        nomebarato = prod
    if preco >= 1000:
        prodcaro += 1   

    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if pergunta == 'N':
        break
print(f'O total gasto na compra é R${totprod:.2f}')
print(f'O total de produtos que custão mais que mil são: {prodcaro} produtos')
print(f'O Nome do produto mais barato é: {nomebarato}')
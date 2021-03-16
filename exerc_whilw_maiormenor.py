'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
 mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

soma = cont = 0
maior = 0
menor = 0
res = 'S'
while res in 'Ss':
    num = int(input('Digite um numero inteiro: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    res = str(input('Quer continurar [S/N]: ')).strip().upper()
media = soma / cont
print('Você Digitou {} numeros e a média foi {}'.format(cont, media))
print('O Maior valor foi {} e o menor valor {}'.format(maior, menor))
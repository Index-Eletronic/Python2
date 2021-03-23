'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
 mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
v = 0
print('-=' * 20)
print('\33[0;30;41m GAME PAR / IMPAR\33[m')
print('-=' * 20)

while True:
    jogador = int(input('Digite um numero: '))
    computador = randint(0, 10)
    tot = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
            tipo = str(input('Par ou Impar [P / I ]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o compurador {computador} no total de {tot}', end='')
    print('DEU PAR 'if tot % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if tot % 2 == 0:
            print('Você GANHOU')
            v += 1
        else:
            print('O PC VENCEU !!!')
            break
    elif tipo == 'I':
        if tot % 2 == 1:
            print('Você GANHOU !!!')
            v += 1
        else:
            print('O PC GANHOU !!!')
            break
    print('Vamos Jogar novamente?')
print(f'GAMER OVER! VOCÊ VENCEU {v} vezes.')



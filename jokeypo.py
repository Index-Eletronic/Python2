# Crie um programa que faça o computador jogar Jokenpõ com vocẽ. ( Pedra Papel Tezoura )
from random import randint
from time import sleep
from tqdm import tqdm
print('''Escolha umas das opções:
                                [ 1 ] - PEDRA
                                [ 2 ] - Papel
                                [ 3 ] -  Tesoura''')
player = int(input('Escolha umas das opções : '))
if player == 1:
    print('Pedra')
elif player == 2:
    print('Ppel')
elif player == 3:
    print('Tesoura')

for i in tqdm(range(10)):
    sleep(1)

comp = randint(1, 3)
if comp == 1:
    print('Pedra')
elif comp == 2:
    print('Papel')
elif comp == 3:
    print('Tesoura')

if comp == player:
    Print('Ninguem Ganhou!')
elif comp  > player:
    print(' Computaodr VENCU')
elif comp < player:
    print('Player Ganhou.')
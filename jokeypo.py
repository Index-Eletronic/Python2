# Crie um programa que faça o computador jogar Jokenpõ com vocẽ. ( Pedra Papel Tezoura
'''from time import sleep
from   tqdm import tqdm
from random import randint
print(' umas das opções:
                                [ 1 ] - PEDRA
                                [ 2 ] - Papel
                                [ 3 ] -  Tesoura')
player = int(input('Escolha umas das opções : '))
if player == 1:
    print('Pedra')
elif player == 2:
    print('Papel')
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
    print('Ninguem Ganhou!')
elif comp  > player:
    print(' Computaodr VENCEU')
elif comp < player:
    print('Player GANHOU.')'''

#=========================================================================================
from  random import randint
from time import sleep
#from  tqdm import tqdm

print('-=' * 20)
print('\33[0;30;41m GAME JOKENPO \33[m')
print('-=' * 20)

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2) # Vai escolher numeros entre 0 e 2
#print('O Computador escolheu {}'.format((itens[computador]))) # Vai mostrar os itens no lugar de numeros... no caso Computador recebe itens.
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO...')
sleep(1)
#for i in tqdm(range(5)):
 #   sleep(1)
print('-=' * 11)
print('Coputador jogou {}'.format(itens[computador]))# Vai mostrar os itens no lugar de numeros... no caso Computador recebe itens.
print('Jogador jogou {}'.format(itens[jogador]))# Vai mostrar os itens no lugar de numeros... no caso Jogador recebe itens.
print('-=' * 11)

if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')

elif computador == 1: #Computador jogou Papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')

elif computador == 2: #Computador jogou Tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
sleep(6)






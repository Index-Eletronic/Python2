# O Computador ira pensar em um numero entre 0 e 10.
#So que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para venceer.
from random import randint

computador = randint(0, 10)
print('Sou seu computador e acabei de pensar num nunmero entre 0 e 10')
print('Será que você consegue adivinhar?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez')
        elif jogador > computador:
            print('Menos...Tente mais uma vez')
print('Acertou com {} tentativas. Parabéns'.format(palpites))

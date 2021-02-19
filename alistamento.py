#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

print('-=' * 30)
print('\33[0;30;41m                  ALISTAMENTO MILITAR                 \33[m')
print('-=' *30)

dataatual = date.today().year
nasc = int(input('Qual foi seu ano de nascimento: '))
idade = dataatual - nasc
print ('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, dataatual))
if idade == 18:
    print('Vocẽ tem que se alistar IMEDIATAMENTO')
elif idade < 18:
    saldo = 18 - idade
    print(' Você ainda nao tem 18 anos. Ainda faltam {} para o alistamento'.format(saldo))
    ano = dataatual + saldo
    print('Seu alistamento será em {} ano'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = dataatual - saldo
    print('Seu alistamento foi em {}'.format(ano))

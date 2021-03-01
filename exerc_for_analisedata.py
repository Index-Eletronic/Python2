#Crie um programa que leia o nascimento de 7 pessoas. No final, mostre quantas pessoas ainda nao atingiram a maior idade e quantas já são maiores.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    dtnasc = int(input('Digite o Ano de nascimento: '))
    idade = atual - dtnasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('A total tivemos {} pessoas maiores de idade'.format(totmaior))
print('A total tivemos {} pessoas menores de idade'.format(totmenor))


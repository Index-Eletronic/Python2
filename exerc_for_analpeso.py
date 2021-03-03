#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maiorp = 0
menorp = 0
for p in range(1,6):
    peso = float(input('Digite o peso da {}  pessoa: '.format(p)))
    if p == 1:
        maiorp = peso
        menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        if peso < menorp:
            menorp = peso
print('O maior peso lido foi de {}Kg.'.format(maiorp))
print('O menor peso lido foi de {}Kg.'.format(menorp))
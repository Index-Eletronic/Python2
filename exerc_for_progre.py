#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. no final mostre os 10 primeiros termos dessa progessão.
termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input(('Digite a razão da PA: ')))
decimo = termo + (11 - 1) * razao

for c in range(termo, decimo, razao):
    print('{}'.format(c), end='-> ')
print('ACABOU')
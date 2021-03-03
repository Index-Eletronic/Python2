#Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo. ( divisiveis por 1 e ele mesmo ).

n = int(input('Digite o numero INTEIRO: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\33[31m', end='')
    print('{}'.format(c), end=' ')
print('\n\33[mO numero {} foi divisivel {} vezes'.format(n, tot))
if tot == 2:
    print('Este numero é PRIMO')
else:
    print('Este numero NÃO É PRIMO')

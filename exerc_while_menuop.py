'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep
print('\33[0; 33; 44m CALCULADORES DE OPÇÔES \33[m')


n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))
opcao = 0
while opcao != 5:

    print('''[ 1 ] - Somar
    [ 2 ] - Multiplicar
    [ 3 ] - Maior
    [ 4 ] - Novos Numeros
    [ 5 ] - Sair do programa ''')
    opcao = int(input(' >>>>> Digite sua opção? '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        multi = n1 * n2
        print('O produto entre {} e {} é {}'. format(n1, n2, multi))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print(' Digite o numero novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando ...')
    else:
        print('Opção invalida, tente novamente')
    print('=-=' * 10)
    sleep(3)
print('Fim do Programa. Volte Sempre')
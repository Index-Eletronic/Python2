
#======================= GUANABARA ==================================================================================
#Escreva um programa que leia um numero inteiro qualquer e peça para usuario escolher qual sera a base de conversao:
# 1 para binário, 2 para octal, 3 para hexadecimal
from time import sleep
print('-=' * 30)
print('\33[0;30;41m                  CONVERSOR DE BASES NUMÉRICAS                 \33[m')
print('-=' *30)

num = int(input('DIGITE UM NUMERO INTEIRO: '))
print(''' ESCOLHA UMA DAS BASES PARA CONVERSÃO:
[ 1 ] - Converter para binário
[ 2 ] - Converter para octal
[ 3 ] - Converter para hexadecimal''')
opcao = int(input('Sua Opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:])) # [2:] faz com que elemine as 2 primeiras casas
elif opcao == 2:
    print('{} convertudo para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida, tente novamente e digite numeros inteiros')
sleep(60)


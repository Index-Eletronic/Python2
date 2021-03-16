'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. No final,
 mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

cont = soma = num = 0
num = int(input('Digite um Numero [999 para parar]: ')) # Foi Adicionado o comando no inicio para ele somar
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um Numero [999 para parar]: '))  # Foi Adicionado o comando no inicio para ele somar
print('Você digitou {} numeros e a soma entre eles foi {}'.format(cont, soma))


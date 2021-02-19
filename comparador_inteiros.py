#Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem
# - O pirmeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais
print('-=' * 20)
print('\33[0;30;41m COMPARADOR DE NUMEROS INTEIROS\33[m')
print('-=' * 20)
n1 = int(input('Digite o primeiro numero inteiro: '))
n2 = int(input('Digite o segundo numero inteiro:'))

if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1:
    print('O segundo valor é maior')
elif n1 == n2:
    print('O valores são identicos')
else:
    print('Digite apenas numeros reais.')
# Dúvida: como colocar como condição se o numero é inteiro ou real?
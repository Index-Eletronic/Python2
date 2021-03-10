'''
Faça um programa que leia um numero qualquer e mostre o seu fatorial.
ex; 5! = 5 x 4 x 3 x 2 x 1 = 120
'''


'''from math import factorial

n = int(input('Digite um Numero pra calcular seu Factorial '))
f = factorial(n)
print('O factorial de {} é {}.'.format(n, f))'''


n = int(input('Digite um Numero pra calcular seu Factorial '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

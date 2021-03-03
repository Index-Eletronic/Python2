# Estruturas em for ( laços de repetição ).
for c in range(1, 6): # faz repetir 01 5x
    print('01')
print('FIM')

for c in range(0, 6): # faz repetir o1 6x
    print('01')
print('FIM')

for c in range(0, 6): # Faz conta 01 02 03..05
    print(c)
print('FIM')

for c in range(6,0, -1): # faz conta de traz para frente.
    print(c)
print('FIM')

for c in range(0, 7, 2): # Faz contar pulando 2.
    print(c)
print('FIM')

n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)
print('FIM')

i = int(input('Digite o numeor do inicio: '))
f = int(input('Digite o numero do Fim; '))
p = int(input('Digite o numero do passo'))
for c in range(i, f+1, p):
    print(c)
print('FIM')

s = 0
for c in range(0, 4): # Soma todos os valores digitados
    n = int(input('Digite o valor: '))
    s += n
print('O somatório de todos os valores  foi {}'.format(s))
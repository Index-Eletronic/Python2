#Refaça o exercicio da tabuada, mostrando o numero que o usuario escolher, só que agora utilizando um laço for.

num =   int(input('Digite o numero pra ver a tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))

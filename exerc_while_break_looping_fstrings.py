'''instrução break e os loopings infinitos a favor das nossas estratégias de código e  fstrings do Python.'''

n = s = 0
while True:
    n = int(input('Escreva um numero [Digite 999 para somar]: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))

#===================== Exemplo usando fstrings =============================
nome = 'jose'
idade = 33
salario = 345.45
print(f'O nome é {nome:-^5} e tem {idade} e ganha R${salario:.2f}')  #f no começo subistitui o .format | ^ Alinha no centro o texto

#Faça um programa que leia o sexo de uma pessoa. mas só aceite os valores M ou F
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Escolha seu sexo [M ou F]: ')).strip().upper()[0] #pega somente a primeira letra
idade = int(input('Digite sua idade'))
while sexo  not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor informe seu sexo novamente: ')).strip().upper()[0]
print('Sexo registrado com sucesso'.format(sexo))

'''nome = str(input('Qual é seu nome? '))
if nome == 'Filipe':
    print('Que nome bonito')
elif nome =='pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cludia Michelle Alicia':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))'''

#=========================================================================
#Escreva um programa para aprovar empréstimo bancário para compra deuma casa.
#O programa vai perguntar o valor da casa,o salario do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestação mensal, sabendo que ela nâo pode exceder 30%do salario ou
#entao o emprestimo sera negado.
'''vlcasa = float(input('Qual valor do imóvel? '))
salario = float(input('Qual renda salarial? '))
anos = int(input('\033[0;33;41mEm quantos meses pretende pagar?\033[m'))
prestacao = vlcasa (anos * 12)
prestmax = salario*1.30
prest = vlcasa/anos

if prest <= prestmax:
    print('Emprestimo liberado .O valor da prestação é R$ {} reais durante {} anos'.format(prest, anos))
elif prest > prestmax:
    print('Emprestimo Negado. O Valor excede a margem consignada.')
else:
    print ('Tente novamente')'''

#=========================================================================================================
#Escreva um programa que leia um numero inteiro qualquer e peça para usuario escolher qual sera a base de conversao:
# 1 para binário, 2 para octal, 3 para hexadecimal



#=========================================================================================================
'''#Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem
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
# Dúvida: como colocar como condição se o numero é inteiro ou real?'''

#=========================================================================================================
#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''import datetime

print('-=' * 20)
print('\33[1;30;41m ANALISADOR DE ALISTAMENTO MILITAR: \33[m')
print('-=' * 20)
tempo = datetime.date.today()
dia = int(input('Dia de nascimento: '))
mes = int(input('Mes de nascimento: '))
ano = int(input('Ano de nascimento: '))
tempo2 = datetime.date(day=dia, month=mes, year=ano)
dif = (tempo - tempo2)/360
if dif > 18:
    print('Você passou do período de alistamento')
elif dif <= 18 and dif == 17:
    print('Voce deve se alistar')
elif dif < 17:
    print("Você ainda nao pode se alistar.")'''






#=========================================================================================================
#Crie um programa que leia duas notas de um aluno e calcule sua média,mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média7.0 ou superior: APROVADO.
n1 = float(input('Digite a primeira nota'))
n2 = float(input(('Digite a segunda nota')))
md = (n1 + n2)/2
if md < 5:
    print('REPROVADO')
elif md >= 5 and md <= 6.9:
    print('RECUPERAÇÃO')
elif md >= 7:
    print('APROVADO')


#=========================================================================================================
#A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordocom a idade;
# Até 9 anos; MIRIM
# Até 14 anos; INFANTIL
# Até 19 anos; Junior
# Até 20 anos; Senior
# Acima: Master

#=========================================================================================================
#Refaça o Desafio dos triangulos, acrescentando o recurso de mostrar que tipode triangulo será formado:
# - Equilatero: todos os lados iguais
# - isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes




#=========================================================================================================
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida.



#=========================================================================================================
#Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# - Á vista dinheiro/cheque: 10% de desconto.
# - Á vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros





#=========================================================================================================
# Crie um programa que faça o computador jogar Jokenpõ com vocẽ. ( Pedra Papel Tezoura )





#=========================================================================================================
#




#=========================================================================================================
#







#========================================================================================================
#


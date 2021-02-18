#Escreva um programa para aprovar empréstimo bancário para compra deuma casa.
#O programa vai perguntar o valor da casa,o salario do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestação mensal, sabendo que ela nâo pode exceder 30%do salario ou
#entao o emprestimo sera negado.

#======== COMO EU FIZ===============================
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

#======== GUANABARA ===============================
print('-=' * 30)
print('\33[0;30;41m                  ANALISADOR DE EMPRÉSTIMOS                 \33[m')
print('-=' *30)

casa = float(input('Valor da Casa: R$ '))
salario = float(input('Salario do Comprador: R$'))
anos = int(input('Quantos anos de Financiamento? '))
prestacao = casa / (anos*12)
minimo = salario * 30 / 100

print('Para pagar uma casa de R${:.2f} reais em {} anos, '.format(casa, anos), end='') # end faz com que o paragrafo fique na mesma linha.
print('a prestação será de {:.2f}'.format(prestacao))
print(' COMPARANDO tem que pagar {} e o minimo é de {}'.format(prestacao,minimo))

if prestacao <= minimo:
    print('\33[0;30;41mEmpréstimo pode ser CONCEDIDO\33[m')
else:
    print('\33[0;30;41mEmpréstimo NÃO pode ser CONCEDIDO\33[m')




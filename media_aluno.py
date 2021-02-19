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
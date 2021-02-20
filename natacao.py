#A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordocom a idade;
# Até 9 anos; MIRIM
# Até 14 anos; INFANTIL
# Até 19 anos; Junior
# Até 20 anos; Senior
# Acima: Master
from datetime import  date

dtatual = date.today().year
nasc = int(input('INSIRA O ANO DE NASCIMENTO DO ATLETA: '))
idade = dtatual - nasc
print('O ATLETA POSSUI {} ANOS'.format(idade))

if idade <= 9:
    print('Este atleta é da categogia MIRIM')
elif idade >=10 and idade <= 14:


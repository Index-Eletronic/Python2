# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida.

altura = float(input('Digite a ALTURA '))
peso = float(input('Digite o peso '))
calc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.2f}'.format(calc))
if calc < 18.5:
    print('ABAIXO DO PESO')
elif calc >= 18.5 and calc < 25:
    print('PESO IDEAl')
elif 25 <= calc < 30:
    print('SOBRE PESO')
elif 30 <= calc < 40:
    print('OBESIDADE')
elif calc > 40:
    print('Obesidade Mórbida')
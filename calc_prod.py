#Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# - Á vista dinheiro/cheque: 10% de desconto.
# - Á vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

prod = float(input('Digite o valor do produto R$: '))
print ('-=' * 30 )
print (''' [ 1 ] - A vista dinheiro
            [ 2 ] - A vista no cartão
            [ 3 ] - Em até 2x no cartão
            [ 4 ] - 3x ou mais no cartão: 20% de juros. ''')
opcao = int(input('Escolha a opção de pagamento : '))

print(' O produto que vccê comprou custa {} reais e seu valor é :'.format(prod), end='')

if
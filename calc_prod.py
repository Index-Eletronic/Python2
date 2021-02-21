#Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# - Á vista dinheiro/cheque: 10% de desconto.
# - Á vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

prod = float(input('Digite o valor do produto R$: '))
print ('-=' * 30 )
print ('''            [ 1 ] - A vista dinheiro
            [ 2 ] - A vista no cartão
            [ 3 ] - Em até 2x no cartão
            [ 4 ] - 3x ou mais no cartão: 20% de juros. ''')
opcao = int(input('Escolha a opção de pagamento : '))

print(' O produto que vccê comprou custa {} reais e seu valor é :'.format(prod), end='')

if opcao == 1:
    valor = prod - (prod * 1.10) + prod
    print('{:.2f}'.format(valor))
elif opcao == 2:
    valor = prod - (prod * 1.05) + prod
    print('{:.2f}'.format(valor))
elif opcao == 3:
    valor = (prod/2)
    print('{:.2f} em 2X de R$ {:.2f}'.format(prod, valor))
elif opcao == 4:
    valor = prod * 1.2
    print('{:.2f}'.format(valor))

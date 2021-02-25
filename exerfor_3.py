#Crie um programa que calcule a soma de todos os numeros impares que são multiplos de 3 e que se encontram no intervalo de 1 a 500.
soma = 0 # Acumulador
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        cont += + 1
        soma += soma + i
print('A soma de todos os {} valores solicitados é: {}'.format(cont, soma))


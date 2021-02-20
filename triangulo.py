#Refaça o Desafio dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
# - Equilatero: todos os lados iguais
# - isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

print('-=' * 20)
print('\33[0;30;41m TIPO DE TRIANGULO \33[m')
print('-=' * 20)

r1 = float(input('Digite o Primeiro seguimento')) # hipotenusa
r2 = float(input('Digite o Segundo seguimento')) # Cateto Oposto
r3 = float(input('Digite o Terceiro seguimento')) #base
area = (r3*r2)/2
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triangulo.')

#Triângulo escaleno
elif r1 != r2 != r3 and r2 != r3:
    triesc =

#Crie uma programa que leia uma frase qualquer e diga se ela é um palìndromo, desconsiderando os espaços.
#Ex; Apos a sopa / A sacada da casa / A torre da derrota / O Lobo ama o bolo / Anotaram a data da maratona.

frase = str(input('Digite uma frase : ')).strip().upper()
palavras = frase.split() # Ira separar as palavras.
junto = ''.join(palavras) # Ira juntar as palvras sem espaços.
inverso = ''
for letra in range(len(junto) -1, -1, -1): #Pega o numero de letas de 'junto' tira 1, Vai até a letra -1 (antes da primeira), e vai voltando uma letra.
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print(' È um palindromo')
else:
    print('Não é um palindromo.')
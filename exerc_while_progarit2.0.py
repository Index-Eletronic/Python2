# #Ler o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
# perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('GERADOR DE PA')
print('-=' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais  = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos vocẽ quer mostrar a mais? '))
print('progressão finalizada com {} termos mostrados'.format(total))
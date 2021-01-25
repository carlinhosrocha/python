from random import randint
from time import sleep
from operator import itemgetter
total = dict()
ranking = dict()
print('='*30)
print('Valores sorteados:')
jog = int(input('Digite quantos jogadores: '))
sleep(1)
for i in range(1, jog + 1):
	x = 'jogador' + str(i)
	total[x] = randint(1, 6)
print('='*30)
print('Jogadores - Pontuação')
for i, l in total.items():
	print(f'{i} - {l} pontos.')
print('='*30)
print('   RANKING DOS JOGADORES   ')
print('-'*30)
ranking = sorted(total.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
	print(f'{i + 1}° lugar: {v[0]} com {v[1]} pontos.')
	sleep(.5)
print('='*30)

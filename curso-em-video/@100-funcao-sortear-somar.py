from time import sleep
from random import randint
# função de sorteio de valores:
def sortear():
	valores = []
	for i in range(0, 5):
		n = randint(0, 9)
		valores.append(n)
	return valores
# função para análise de valores:
def soma(lista):
	print('Os valores sorteados foram: ', end='')
	par = 0
	for k, v in enumerate(lista):
		sleep(0.3)
		print(f'{v} ', end='', flush=True)
		if v % 2 == 0:
			par += v
	print('PRONTO!')
	print(f'Somando os valores pares de {lista}, temos {par}.')
# programa principal:
val = sortear()
soma(val)	

from time import sleep
# função para escrever linha na tela
def l(x):
	print('=' * x)
# função para descobrir o maior valor
def maior(* num): # desempacotamento de parâmetros
	l(40)
	print('Analisando os valores passados:')
	for i in num:
		print(f'{i} - ', end='', flush=True)
		if i == num[0]:
			max = i
		elif i > max:
			max = i
	if len(num) == 0:
		max = 0
	print('FIM')
	print(f'Foram informados {len(num)} valores ao todo.')
	print(f'O maior entre eles é {max}.')
	l(40)
##########################################################
# programa principal
maior(2, 9, 4 , 5, 7, 1)
sleep(1)
maior(4, 7, 0)
sleep(1)
maior(1, 2)
sleep(1)
maior(6)
sleep(1)
maior()

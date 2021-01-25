from time import sleep
def contador():
	print('=-'*15)
	print('Contagem de 1 à 10 de 1 em 1:')
	for i in range(1, 11, 1):
		sleep(.5)
		print(f'{i} ', end='', flush=True)
	sleep(.5)
	print('FIM!')
	print('=-'*15)
	print('Contagem de 10 à 0 de 2 em 2:')
	for i in range(10, 0, -2):
		print(f'{i} ', end='', flush=True)
		sleep(.5)
	print('FIM!')
def usuario(i, f, p):
	print('=-'*15)
	for i in range(i, f, p):
		print(f'{i} ', end='', flush=True)
		sleep(.5)
	print('FIM!')
# programa principal
contador()
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
usuario(i, f, p)
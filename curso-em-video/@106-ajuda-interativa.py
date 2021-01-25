def ajuda():
	while True:
		print('='*30)
		print(' SISTEMA DE AJUDA PyHELP')
		print('='*30)
		n = str(input('Função ou Biblioteca >> '))
		if n == 'FIM' or n == 'fim':
			print('='*30)
			print('Programa encerrado...')
			print('='*30)
			break
		else:
			print('-'*50)
			print(help(n))
			print('#'*50)
# programa principal:
ajuda()
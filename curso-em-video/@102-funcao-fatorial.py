# função para cálculo de fatorial:
def fatorial(num, show=True):
	"""
		=======================================
		fatorial(num, show):
		num -> fatorial a ser calculado
		show -> parâmetro para exibir o cálculo
		=======================================
	"""
	print('=' * 30)
	print(f'O fatorial de {num} é:')
	fat = 1
	for i in range(1, num + 1):
		fat *= i
		if show == True:
			print(f'{i} x ', end='')
	if show:
		print(f'igual a: {fat}')
	else:
		print(fat)
# função principal:
n = int(input('Qual número quer calcular o fatorial? '))
t = str(input('Deseja mostrar o cálculo? [S/N]: ')).upper()[0]
if t in 'S':
	fatorial(n)
else:
	fatorial(n, show=False)
print(help(fatorial))
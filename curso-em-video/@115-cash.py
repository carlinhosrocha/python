def resumo(p, x=10, y=5):
	d = p * 2
	m = p / 2
	a = p + (p * x/100)
	r = p - (p * y/100)
	print('='*30)
	print(f'{"RESUMO DO VALOR":^30}')
	print('='*30)
	print(f'Preço analisado: {"R$":>8}{p:>1}')
	print(f'Dobro do preço: {"R$":>8}{d:>1}')
	print(f'Metade do preço: {"R$":>8}{m:>1}')
	print(f'{x}% de aumento: {"R$":>8}{a:>1}')
	print(f'{y}% de desconto: {"R$":>8}{r:>1}')
	print('-'*30)

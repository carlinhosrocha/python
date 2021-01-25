def dobro(n, m='R$'):
	x = n * 2
	y = f'{m}{x:.2f}'.replace('.', ',')
	return y
def moeda(n, m='R$'):
	x = f'{m}{n:.2f}'.replace('.', ',')
	return x
def metade(n, m='R$'):
	x = n / 2
	y = f'{m}{x:.2f}'.replace('.', ',')
	return y
def aumento(n, m='R$', taxa=10):
	x = n * taxa/100
	y = f'{m}{(n + x):.2f}'.replace('.', ',')
	return y
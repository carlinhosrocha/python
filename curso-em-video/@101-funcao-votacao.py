# função checa idade:
print('=' * 30)
def voto(nasc):
	"""
	DOCSTRING
	"""
	from datetime import date
	idade = date.today().year - nasc
	print(f'Com {idade} anos: ', end='')
	if idade < 16:
		print('NÃO VOTA!')
	elif idade < 18:
		print('VOTO OPCIONAL!')
	elif idade < 70:
		print('VOTO OBRIGATÓRIO!')
	else:
		print('VOTO OPCIONAL!')
# programa principal:
voto(int(input('Em que ano você nasceu? ')))
print('='*30)
print(help(voto))

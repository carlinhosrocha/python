def nota(* notas, sit=False):
	"""
	== notas: lista com as notas informadas
	== sit=False: não exibe a situção
	-> função nota recebe uma série de notas:
	- informa a quantidade de notas
	- exibe a maior nota
	- exibe a menor nota
	- exibe a média
	- mostra a situção da média (opcional)
	"""
	grade = {}
	soma = 0
	total = len(notas)
	for i in notas:
		soma += i
		if i == notas[0]:
			maxi = i
			mini = i
		elif i > maxi:
			maxi = i
		elif i < mini:
			mini = i
	media = soma / len(notas)
	if media < 6:
		situ = 'RUIM'
	elif media < 8:
		situ = 'RAZOÁVEL'
	else:
		situ = 'BOA'
	grade['total:'] = total
	grade['maior:'] = maxi
	grade['menor:'] = mini
	grade['média:'] = media
	if sit:
		grade['situação:'] = situ
	print(grade)
# programa principal:
print('='*40)
nota(6, 5, 4, 3, 10, 10, 10, 10, sit=1)
print('='*40)
print(help(nota))
print('='*40)
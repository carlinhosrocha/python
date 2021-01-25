notas = {} # dicionário em python
print('='*25)
notas['nome'] = str(input('Nome: '))
notas['média'] = float(input(f'Média de {notas["nome"]}: '))
if notas['média'] >= 7:
	notas['situação'] = 'Aprovado'
elif 5 <= notas['média'] < 7:
	notas['situação'] = 'Recuperação'
else:
	notas['situação'] = 'Reprovado'
print('='*25)
for k, v in notas.items(): # semelhante ao enumerate das listas
	print(f'- {k} é igual à {v}.')
print('='*25)

from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input('Digite o nome: '))
cadastro['nascimento'] = int(input(f'Ano de Nascimento de {cadastro["nome"]}: '))
cadastro['idade'] = datetime.now().year - cadastro['nascimento']
cadastro['carteira'] = int(input('Carteira de Trabalho [0 não tem]: '))
if cadastro['carteira'] == 0:
	print('='*30)
	for k, v in cadastro.items():
		print(f'- {k} tem valor {v}.')
	print('='*30)
	print('Cadastro finalizado...')
else:
	cadastro['ano'] = int(input(f'Ano que {cadastro["nome"]} foi contratado(a): '))
	cadastro['salário'] = float(input(f'Salário Atual de {cadastro["nome"]}: R$'))
	cadastro['aposentadoria'] = cadastro['ano'] - cadastro['nascimento'] + 35
if cadastro['carteira'] != 0:
	print('='*30)
	for k, v in cadastro.items():
		print(f'- {k} tem valor {v}.')
	print('='*30)
	print('Cadastro finalizado...')
	
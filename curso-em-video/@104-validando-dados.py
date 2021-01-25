# funcao para validação de dados:
def validar(n):
	n.strip()
	while True:
		if n.isnumeric():
			return int(n)
		else:
			print('ERRO! Digite um número válido!')
			n = str(input('Digite corretamente: '))
			continue
# programa principal:
print('=' * 30)
n = validar('Digite um número: ')
print(f'Você digitou o número {n}.')

time = []
jogador = {}
gols = []
flag = True
print('=='*20)
while flag:
	jogador['nome'] = str(input("Nome do Jogador: "))
	jogador['partidas'] = int(input(f"Quantas partidas {jogador['nome']} jogou: "))
	for i in range(0, jogador['partidas']):
		gols.append(int(input(f'-> Quantos gols na partida {i}: ')))
	jogador['gol'] = gols[:]
	jogador['total'] = sum(gols)
	time.append(jogador.copy())
	gols.clear()
	print('=='*20)
	while True:
		resp = str(input('Quer continuar?[S/N]: '))
		if resp in 'Ss':
			break
		elif resp in 'Nn':
			flag = False
			break
		print('Opção inválida...')
print('='*40)
print('cod | nome |   jogos   |   gols   |   total')
print('-'*40)
x = 0
for k, v in enumerate(time):
	print(f'{k:>3} ', end='')
	for d in v.values():
		print(f'{str(d):<10}', end='')
	print()
	#print(f' {x} - {i["nome"]} -  {i["gol"]} -  {sum(i["gol"])}')
	#x += 1
print('-'*40)
while True:
	dado = int(input('Mostrar dados de qual jogador?[999 para parar]: '))
	if dado == 999:
		print('<<< VOLTE SEMPRE! >>>')
		print('*'*40)
		break
	if dado >= len(time):
		print('ERRO! Não existe o jogador...')
		continue
	print('-'*40)
	print(f'-- LEVANTAMENTO DO JOGADOR: {time[dado]["nome"]} --')
	x = 1
	for i in time[dado]['gol']:
		print(f'  -> No jogo {x} fez {i} gols.')
		x += 1
	print('-'*40)
print('-'*40)
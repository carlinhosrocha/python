jogador = dict() # dicionário para armazenar dados do jogados
gols = list() # dicionário que armazena os gols
jogador['nome'] = str(input('Nome do Jogador: '))
jogador['jogos'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0, jogador['jogos']):
	gols.append(int(input(f' - Quantos gols na partida {i}: ')))
jogador['gol'] = gols.copy()
jogador['total'] = sum(gols)
print('='*30)
print(jogador)
print('='*30)
for k, v in jogador.items():
	print(f'O campo {k} tem valor {v}.')
print('='*30)
print(f'O jogador {jogador["nome"]} jogou {jogador["jogos"]} partidas.')
x = 0
for b in jogador['gol']:
	print(f' => Na partida {x}, fez {b} gols.')
	x += 1
print(f'Foi um total de {jogador["total"]}.')

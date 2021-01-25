tabela = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atlético-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('='*33)
print(f'Os primeiros cinco colocados são: ')
print('='*33)
for i in range(0, 5):
    print(f'{i+1}° - {tabela[i]}')
print('='*33)
print(f'Os últimos quatro colocados são: ')
print('='*33)
for c in range(-1, -5, -1):
    print(f'{21+c}° - {tabela[c]}')
ordenados = sorted(tabela)
y = 1
print('='*33)
print('Os times em ordem alfabética são: ')
print('='*33)
for x in ordenados:
    print(f'{y}° - {x}')
    y += 1
print('='*33)
print(f'A chapecoense está na {tabela.index("Chapecoense")+1}° posição.')
print('='*33)

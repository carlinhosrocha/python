print('='*30)
print('  PROGRESSÕES ARITMÉTICA  ')
print('='*30)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
decimo = termo + (razao * (10 - 1))
for i in range(termo, (decimo+1), razao):
    print(f'{i} -> ', end=' ')
print('Fim da PA')

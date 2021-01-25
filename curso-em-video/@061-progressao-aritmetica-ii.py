print('='*15)
print(' GERADOR DE PA ')
print('='*15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
i = 1
pa = 0
print('Os dez primeiros termos da PA são: ')
while i < 10:
    if i == 1:
        print(f'{primeiro} - ', end='')
    pa = primeiro + (i * razao)
    print(f'{pa}', end='')
    print(' - FIM' if pa == (primeiro + (9 * razao)) else ' - ', end='')
    i += 1

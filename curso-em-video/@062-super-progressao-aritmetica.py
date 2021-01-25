print('=' * 20)
print(' GERADOR PA 1.0')
print('=' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
mostrar = 10
i = 0
a = 0
cont = mostrar
while i <= (mostrar - 1):
    pa = primeiro + (i * razao)
    i += 1
    print(f'{pa}', end='')
    print(f' - ' if pa != (primeiro + ((mostrar - 1) * razao)) else ' - FIM ', end='')
    if pa == (primeiro + ((mostrar - 1) * razao)):
        novo = int(input('\nDigite mais quantos termos a serem mostrados: '))
        mostrar = mostrar + novo
        cont = mostrar
        if novo == 0:
            break
print('-'*30)
print(f'Foram mostrados {cont} termos.')

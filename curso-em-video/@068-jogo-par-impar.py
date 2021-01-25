from random import randint # geracao de valores através da lib
a = 24
print('='*a)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('='*a)
vitoria = 0
while True: 
    jog = int(input('Digite um número: '))
    esc = str(input('Par ou Ímpar:[P/I] ')).strip()[0]
    if esc in 'Pp':
        jogador = 0
    elif esc in 'Ii':
        jogador = 1
    else:
        print('Opção inválida...')
        continue # volta para o laço
    comp = randint(1, 10)
    num = jog + comp
    print(f'Você jogou {jog} e o computador jogou {comp} totalizando {num}.')
    if num % 2 == 0:
        sorte = 0
    else:
        sorte = 1
    if jogador == sorte:
        vitoria += 1
        print('Jogador venceu...')
    else:
        print('Jogador perdeu...')
        break
print(f'O total de vitótia(s) do jogador foi de {vitoria}.')

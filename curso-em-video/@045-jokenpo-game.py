from random import randint
from time import sleep
print('='*13)
print('SUAS OPÇÕES:')
print('[1] PEDRA')
print('[2] PAPEL')
print('[3] TESOURA')
print('='*13)
jogador = int(input('Jogador: '))
computador = randint(1, 3) #computador sorteia número
if jogador == 1 or jogador == 2 or jogador == 3:
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)
else:
    print('Opção inválida...tente novamente!')
if jogador == computador:
    print('Deu empate....')
    if jogador == 1 and computador == 1:
        print('Computador e Jogador jogaram PEDRA!')
    elif jogador == 2 and computador == 2:
        print('Computador e Jogador jogaram PAPEL!')
    else:
        print('Computador e Jogador jogaram TESOURA!')
elif jogador == 1 and computador == 2:
    print('Computador jogou PAPEL...\nJogador jogou PEDRA...\nJogador PERDEU! :(')
elif jogador == 2 and computador == 3:
    print('Computador jogou TESOURA...\nJogador jogou PAPEL...\nJogador PERDEU!... :(')
elif jogador == 3 and computador == 1:
    print('Computador jogou PEDRA...\nJogador jogou TESOURA...\nJogador PERDEU!... :(')
elif jogador == 2 and computador == 1:
    print('Computador jogou PEDRA...\nJogador jogou PAPEL...\nJogador VENCEU!... :)')
elif jogador == 3 and computador == 2:
    print('Computador jogou PAPEL...\nJogador jogou TESOURA...\nJogaodr VENCEU!... :)')
elif jogador == 1 and computador == 3:
    print('Computador jogou TESOURA...\nJogador jogou PEDRA...\nJogador VENCEU!... :)')

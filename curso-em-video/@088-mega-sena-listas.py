from time import sleep
from random import randint
jogo = []
print('='*40)
print(f'{"JOGOS NA MEGA-SENA":^40}')
print('='*40)
n = int(input('Quantos jogos você quer? '))
sleep(0.2)
print(f'{"=========== Sorteando Jogos ============"}')
for i in range(1, n+1):
    for c in range(0, 6):
        x = randint(1, 60)
        jogo.append(x)
    sleep(1)
    print(f'Jogo número {i}: {jogo}')
    jogo.clear()
sleep(0.2)
print('============== Boa Sorte :) ============')
#-----------------------------------------------------#
lista = list()
jogos = []
cont = 0
print('-'*30)
print('       Joga na Mega Sena      ')
print('-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont>= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('='*7, f'Sorteando {quant} Jogos ', '='*7)
for o, l in enumerate(jogos):
    print(f'Jogo {o}: {l}')
print('='*30)

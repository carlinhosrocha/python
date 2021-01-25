from random import randint #modulo de 'sorteio' de numeros
from time import sleep #modulo de tempo
print(40*'=')
print('Tente adivinhar qual número eu pensei!!')
print(40*'=')
comp = randint(0, 5) #computador sorteia um numero
num = int(input('Digite um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(3) #delay de 3 segundos
if(comp == num):
    print('Parabéns!! Você acertou!')
else:
    print(f'Sinto muito, você errou! Escolhi o número {comp}.')

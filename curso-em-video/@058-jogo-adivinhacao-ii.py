from random import randint #modulo de sorteio de numero aleatorio
print('Sou seu computador...')
num = randint(0, 10)#sorteio do numero
cont = 0
print('Pensei em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
palpite = int(input('Qual seu palpite? '))
while True: #inicio do laço de repetição
    if palpite == num: #checa se jogador acertou
        print('Parabéns! Você acertou!')
        cont += 1 #conta as tentativas
        break #comando que interronpe o laço do ciclo
    if palpite < num: #avalia se palpite é menor que numero randomizado
        palpite = int(input('Digite um número maior! Tente novamente: '))
        cont += 1
    if palpite > num: #avalia se palpite é maior que numero randomizado
        palpite = int(input('Digite um número menor! Tente novamente: '))
        cont += 1
print('Você usou {} tentativa(s).'.format(cont))

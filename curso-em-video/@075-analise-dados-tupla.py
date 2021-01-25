nove = 0
tres = 0
par = 0
for c in range(1, 5):
    num = int(input(f'Digite o {c}° elemento: '))
    if num == 9:
        nove += 1
    if num == 3:
        tres = c
    if num % 2 == 0:
        par += 1
print(f'O valor 9 apareceu {nove} vezes.')
print(f'O valor 3 apareceu na {tres}° posição.')
print(f'Os valores pares digitados totais são {par}.')
#------------Resplução------------------#
print('=-'*15)
num = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')), int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')))
print('Valores digitados: ')
for i in num:
    print(i)
print('-'*10)
print(f'O valor 9 aparece {num.count(9)}.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)}° posição.')
else:
    print('O valor três não foi digitado.')
pares = 0
for n in num:
    if n % 2 == 0:
        pares += 0;
print(f'Os valores pares digitados ao todo são: {pares}.')

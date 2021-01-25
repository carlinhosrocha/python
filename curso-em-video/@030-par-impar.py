from time import sleep
num = int(input('Digite um número: '))
print('PROCESSANDO...')
sleep(1)
if(num % 2 == 0):
    print(f'O número {num} é PAR!')
else:
    print(f'O número {num} é ÍMPAR!')

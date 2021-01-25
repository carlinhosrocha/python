cont = 0
num = int(input('Digite um número: '))
print(f'O número {num} tem os seguintes divisores: ')
for i in range(1, num + 1):
    if num % i == 0:
        cont += 1
        print(f'{i} - ', end=' ')
print(' FIM')
if cont == 2:
    print(f'O número digitado é PRIMO!!')
else:
    print(f'O número {num} NÃO é PRIMO!')

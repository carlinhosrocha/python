total = []
par = []
impar = []
flag = 0
while flag == 0:
    n = int(input('Digite um valor: '))
    total.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    rasp = str(input('Deseja continuar?[N/S]: '))
    if rasp in 'Nn':
        break
print(f'A lista completa é {total}.')
print(f'Os valores pares são {par}.')
print(f'Os valores impares são {impar}.')
#-------------------------------------------------------#
num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'A lista completa é {num}).')
print(f'A lista de pares é {pares}.')
print(f'A lista de impares é {impares}.')

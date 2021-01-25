from math import factorial #importando da biblioteca math uma função
#------------------------ Versão Carlos --------------------------#
num = int(input('Digite um número para calcular seu Fatorial: '))
fatorial = 1
cont = 1
print(f'{cont} x ', end="")
while cont <= num:
    fatorial = fatorial * cont
    cont += 1        
    if cont != num:
        print(f'{cont} x ', end="")    
print(f'{num} = {fatorial}')
#--------------------- Versão Guanabara -------------------------#
n = int(input('Digite um número: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))
#--------------------- Versão Guanabara 2.0 ---------------------#
n = int(input('Digite um número para o cálculo de fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print('{}'.format(f))
#-----------------------------------------------------------------#

num = int(input('Digite um número: '))
print('='*20)
print('[1] para binário')
print('[2] para octal')
print('[3] para hexadecimal')
print('='*20)
escolha = int(input('Qual a base a ser convertida? '))
if(escolha == 1):
    print(f'O número {num} em binário é {bin(num)[2:]}.')
elif(escolha == 2):
    print(f'O número {num} em octal é {oct(num)[2:]}.')
elif(escolha == 3):
    print(f'O número {num} em hexadecimal é {hex(num)[2:]}.')
else:
    print('Opção inválida...')

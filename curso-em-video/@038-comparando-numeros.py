num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
maior = num1 if num1 > num2 else num2
if(num1 != num2):
    print(f'O maior número é {maior}.')
else:
    print('Os dois números são iguais.')

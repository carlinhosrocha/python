num = list()
flag = 0
while flag == 0:
    n = int(input('Digite um valor: '))
    if n in num:
        print('Esse valor já foi digitado. Tente outro...')
    else:
        num.append(n)
    rasp = ' '
    while rasp not in 'NnSs':
        rasp = input('Quer continuar?[S/N]: ')
        if rasp in 'Nn':
            flag = 1
        elif rasp in 'Ss':
            continue
        else:
            print('Opção inválida. Tente novamente...')
print(f'Você digitou {len(num)} valores.')
num.sort(reverse = True) # valores em ordem descrescente
print(f'Os valores na lista em ordem descrecente são {num}.')
if 5 in num:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não foi encontrado.')

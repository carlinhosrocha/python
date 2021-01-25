num = []
maior = menor = 0
cmais = cmenos = 0
for i in range(0, 5):
    num.append(int(input(f'Digite um número para a posição {i}: ')))
    if i == 0:
        maior = menor = num[i]
    else:
        if num[i] > maior:
            maior = num[i]
        if num[i] < menor:
            menor = num[i]
print(f'Você digitou os seguintes valores: ', end='')
for x in num:
    print(f' {x} - ', end='')
print('FIM')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for y in num:
    if y == maior:
        print(f'{cmais}...')
    cmais += 1
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for z in num:
    if z == menor:
        print(f'{cmenos}...')
    cmenos += 1

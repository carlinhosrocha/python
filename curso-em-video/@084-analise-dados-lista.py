flag = 0
cadastrado = []
total = []
mai = men = 0
while flag == 0:
    nome = str(input('Digite o nome: '))
    peso = float(input('Digite o peso: '))
    cadastrado.append(nome)
    cadastrado.append(peso)
    if len(total) == 0:
        mai = men = cadastrado[1]
    else:
        if cadastrado[1] > mai:
            mai = cadastrado[1]
        if cadastrado[1] < men:
            men = cadastrado[1]
    total.append(cadastrado[:]) #faz uma cópia da lista
    cadastrado.clear() #apaga os elementos da lista
    sair = ' '
    while sair not in 'NnSs':
        sair = str(input('Quer continuar? [S/N]: ')).strip()
        if sair in 'Ss':
            break
        elif sair in 'Nn':
            flag = 1
print(f'Ao todo você cadastrou {len(total)} pessoas.')
print(f'O maior peso foi de {mai}kg. A pessoa foi ', end='')
for i in total:
    if i[1] == mai:
        print(f'[{i[0]}] ', end='')
print()
print(f'O menor peso foi de {men}kg. A pessoa foi ', end='')
for i in total:
    if i[1] == men:
        print(f'[{i[0]}] ', end='')
